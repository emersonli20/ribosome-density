import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import h5py
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--filled_membrane_filename", type=str, required=True, help="output path of filled membrane file")
parser.add_argument("-i", "--indices_filename", type=str, required=True, help="output path of nonzero indices file")
parser.add_argument("-m", "--mem_brushed", type=str, required=True, help="path of the brushed membrane file")
parser.add_argument("-x", "--x_dim", type=int, required=True, help="~680")
parser.add_argument("-y", "--y_dim", type=int, required=True, help="~960")
parser.add_argument("-z", "--z_dim", type=int, required=True, help="~256")

args = parser.parse_args()
filled_membrane_filename = args.filled_membrane_filename
indices_filename = args.indices_filename
mem_brushed = args.mem_brushed
x_dim = args.x_dim
y_dim = args.y_dim
z_dim = args.z_dim

#3d dataset of voxels
# d = np.zeros((960,686,256))

# load surface coefficients
coeffs_1 = np.loadtxt("coeffs_1.csv", delimiter=",")
coeffs_2 = np.loadtxt("coeffs_2.csv", delimiter=",")

membrane_coords = np.loadtxt(mem_brushed, delimiter=",")
coeffs_1 = np.loadtxt("coeffs_1.csv", delimiter=",")
coeffs_2 = np.loadtxt("coeffs_2.csv", delimiter=",")

x_all = membrane_coords[:,0]
y_all = membrane_coords[:,1]
z_all = membrane_coords[:,2]

x_min = int(np.min(x_all))
y_min = int(np.min(y_all))
z_min = int(np.min(z_all))
x_max = int(np.max(x_all))
y_max = int(np.max(y_all))
z_max = int(np.max(z_all))

d = np.zeros((x_dim,y_dim,z_dim))
print("d shape: {}".format(d.shape))

top_coeffs = coeffs_1 if coeffs_1[0] > coeffs_2[0] else coeffs_2
bottom_coeffs = coeffs_2 if coeffs_1[0] > coeffs_2[0] else coeffs_1

print("top_coeffs: {}".format(top_coeffs))
print("bottom_coeffs: {}".format(bottom_coeffs))

#create a grid
# TODO: change these to 441, 844, 250 since we only the range where the ribosome points exist?
# translate these to start from 0?

x = np.arange(0,x_dim,1)
y = np.arange(0,y_dim,1)
z = np.arange(0,z_dim,1)

#x = np.arange(x_min, x_max+1)
#y = np.arange(y_min, y_max+1)
#z = np.arange(z_min, z_max+1)

# xx,yy,zz = np.meshgrid(x,y,z, indexing = 'xy')
xx,yy,zz = np.meshgrid(x,y,z, indexing = 'ij')
print("xx shape: {}".format(xx.shape))

#functions
bottom_surface = bottom_coeffs[0] + bottom_coeffs[1]*xx + bottom_coeffs[2]*yy +bottom_coeffs[3]*(xx**2) + bottom_coeffs[4] * (xx*yy) + bottom_coeffs[5] * (yy**2) #(xx**3) + bottom_coeffs[6] * (xx**2 * yy) + bottom_coeffs[7] * (xx**4) + bottom_coeffs[8] * (xx**3 * yy)
top_surface = top_coeffs[0] + top_coeffs[1]*xx + top_coeffs[2]*yy +top_coeffs[3]*(xx**2) + top_coeffs[4] * (xx*yy) + top_coeffs[5] * (yy**2) #(xx**3) + top_coeffs[6] * (xx**2 * yy) + top_coeffs[7] * (xx**4) + top_coeffs[8] * (xx**3 * yy)

#create mask
mask = (zz < top_surface) & (zz > bottom_surface) & (xx > x_min) & (xx < x_max) & (yy > y_min) & (yy < y_max) & (zz > z_min) & (zz < z_max)

#apply the mask
d[mask] = 4
d[~mask] = 0


#reshape the dataset by z-slices
# z, x, y
# d = d.transpose(2,1,0)
d = d.transpose(2,0,1)
print("d shape: {}".format(d.shape))

filled_membrane = d.reshape(d.shape[0], -1)
print("filled_membrane shape: {}".format(filled_membrane.shape))

indices = np.nonzero(d)

np.savetxt(filled_membrane_filename, filled_membrane, delimiter = ',')

# x_i = indices[1]
# y_i = indices[2]
z_i = indices[0]
x_i = indices[1]
y_i = indices[2]

indices_arr = np.column_stack((x_i[:,None], y_i[:,None], z_i[:,None]))
print(indices_arr.shape)
np.savetxt(indices_filename, indices_arr, delimiter = ',')

# next step: convert csv to hdf
# h5f = h5py.File('data.h5', 'w')
# h5f.create_dataset('dataset_1', data = d)
# h5f.close()
# testing purposes 
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.scatter3D(x_i, y_i,z_i);
# plt.savefig('filled.png')

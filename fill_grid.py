import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import h5py

#3d dataset of voxels
# d = np.zeros((960,686,256))
d = np.zeros((686,960,256))

# load surface coefficients
coeffs_1 = np.loadtxt("coeffs_1.csv", delimiter=",")
coeffs_2 = np.loadtxt("coeffs_2.csv", delimiter=",")

top_coeffs = coeffs_1 if coeffs_1[0] > coeffs_2[0] else coeffs_2
bottom_coeffs = coeffs_2 if coeffs_1[0] > coeffs_2[0] else coeffs_1

print("top_coeffs: {}".format(top_coeffs))
print("bottom_coeffs: {}".format(bottom_coeffs))


#create a grid
# TODO: change these to 441, 844, 250 since we only the range where the ribosome points exist?
# translate these to start from 0?

x = np.arange(0,686,1)
y = np.arange(0,960,1)
z = np.arange(0,256,1)
# xx,yy,zz = np.meshgrid(x,y,z, indexing = 'xy')
xx,yy,zz = np.meshgrid(x,y,z, indexing = 'ij')
print("xx shape: {}".format(xx.shape))

#functions
bottom_surface = bottom_coeffs[0] + bottom_coeffs[1]*xx + bottom_coeffs[2]*yy +bottom_coeffs[3]*(xx**2) + bottom_coeffs[4] * (xx*yy) + bottom_coeffs[5] * (xx**3) + bottom_coeffs[6] * (xx**2 * yy) + bottom_coeffs[7] * (xx**4) + bottom_coeffs[8] * (xx**3 * yy)
top_surface = top_coeffs[0] + top_coeffs[1]*xx + top_coeffs[2]*yy +top_coeffs[3]*(xx**2) + top_coeffs[4] * (xx*yy) + top_coeffs[5] * (xx**3) + top_coeffs[6] * (xx**2 * yy) + top_coeffs[7] * (xx**4) + top_coeffs[8] * (xx**3 * yy)

#create mask
mask = (zz < top_surface) & (zz > bottom_surface)

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

np.savetxt('filled_membrane.csv', filled_membrane, delimiter = ',')

# x_i = indices[1]
# y_i = indices[2]
z_i = indices[0]
x_i = indices[1]
y_i = indices[2]

indices_arr = np.column_stack((x_i[:,None], y_i[:,None], z_i[:,None]))
print(indices_arr.shape)
np.savetxt('indices.csv', indices_arr, delimiter = ',')

# next step: convert csv to hdf
# h5f = h5py.File('data.h5', 'w')
# h5f.create_dataset('dataset_1', data = d)
# h5f.close()
# testing purposes 
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.scatter3D(x_i, y_i,z_i);
# plt.savefig('filled.png')

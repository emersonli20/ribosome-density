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
bottom_coeffs = coeffs_2 if coeffs_1[0] < coeffs_2[0] else coeffs_1

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
bottom_surface = 459.33 + 2.7631*xx - 1.41*yy +0.0025207*(xx**2) - 0.001111 * (xx*yy) 
top_surface = 662.72 + 3.0544*xx - 1.4659*yy + 0.0025797*(xx**2) - 0.0011323*(xx*yy) 

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

# np.savetxt('indices.csv', indices, delimiter = ',')
# np.savetxt('filled_membrane.csv', filled_membrane, delimiter = ',')

# x_i = indices[1]
# y_i = indices[2]
# z_i = indices[0]
x_i = indices[1]
y_i = indices[2]

#next step: convert csv to hdf
h5f = h5py.File('data.h5', 'w')
h5f.create_dataset('dataset_1', data = d)

# testing purposes 
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.scatter3D(x_i, y_i,z_i);
# plt.savefig('filled.png')

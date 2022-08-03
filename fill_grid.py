import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#3d dataset of voxels
d = np.zeros((960,686,256))

#create a grid
x = np.arange(0,686,1)
y = np.arange(0,960,1)
z = np.arange(0,256,1)
xx,yy,zz = np.meshgrid(x,y,z, indexing = 'xy')

#functions
bottom_surface = 459.33 + 2.7631*xx -1.41*yy +0.0025207*(xx**2) - 0.001111 * (xx*yy) 
top_surface = 662.72 + 3.0544*xx - 1.4659*yy + 0.0025797*(xx**2) - 0.0011323*(xx*yy) 

#create mask
mask = (zz < top_surface) & (zz > bottom_surface)

#apply the mask
d[mask] = 4
d[~mask] = 0

#reshape the dataset by z-slices
d = d.transpose(2,0,1)

indices = np.nonzero(d)
np.savetxt('indices.csv', indices, delimiter = ',')

x_i = indices[2]
y_i = indices[1]
z_i = indices[0]

#next step: convert csv to hdf

#testing purposes
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(x_i, y_i,z_i);
plt.savefig('filled.png')

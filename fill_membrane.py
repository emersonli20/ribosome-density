import numpy as np

membrane_coords = np.loadtxt("5991_L2_ts001_1.5.csv", delimiter=",")
coeffs_1 = np.loadtxt("coeffs_1.csv", delimiter=",")
coeffs_2 = np.loadtxt("coeffs_2.csv", delimiter=",")

x = membrane_coords[:,0]
y = membrane_coords[:,1]
z = membrane_coords[:,2]

x_min = np.min(x)
y_min = np.min(y)
z_min = np.min(z)
x_max = np.max(x)
y_max = np.max(y)
z_max = np.max(z)

print(membrane_coords.shape)
print(coeffs_1.shape)
print(coeffs_2.shape)

x_range = np.arange(x_min,x_max+1)
print(x_range.shape)
y_range = np.arange(y_min,y_max+1)
print(y_range.shape)
z_range = np.arange(z_min,z_max+1)

x_grid = x_range[:,None] + np.zeros((y_range.shape[0]))
print(x_grid.shape)

y_grid = y_range[:,None] + np.zeros((x_range.shape[0]))
print(y_grid.shape)
y_grid = y_grid.T

np.stack((x_grid[:,:,None], y_grid[:,:,None], axis=2)
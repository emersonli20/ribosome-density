import numpy as np
import pandas as pd
import h5py

arr = 3* np.random.rand(200,960,686)
'''n, m = arr.shape
num_shells = int(m/3)
shells_coords = np.array(np.hsplit(arr, num_shells))
print(shells_coords.shape)'''
h5f = h5py.File('data.h5', 'w')
h5f.create_dataset('dataset_1', data = arr)

import numpy as np
import pandas as pd
import h5py
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-x", "--x_dim", type=int, required=True)

args = parser.parse_args()

x_dim = args.x_dim

arr = np.loadtxt("filled_membrane.csv", delimiter=",")
arr = arr.reshape(arr.shape[0], x_dim, -1)
arr = arr.transpose(0,2,1)

print(arr.shape)

h5f = h5py.File('data_6.h5', 'w')
h5f.create_dataset('dataset_1', data = arr)
# arr = 3* np.random.rand(200,960,686)
'''n, m = arr.shape
num_shells = int(m/3)
shells_coords = np.array(np.hsplit(arr, num_shells))
print(shells_coords.shape)'''

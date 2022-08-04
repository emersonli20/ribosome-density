import numpy as np
import h5py
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--filename", type=str, required=True)
parser.add_argument("-o", "--output", type=str, required=True)
parser.add_argument("-x", "--x_dim", type=int, required=True)

args = parser.parse_args()

filename = args.filename
output = args.output
x_dim = args.x_dim

arr = np.loadtxt(filename, delimiter=",")
arr = arr.reshape(arr.shape[0], x_dim, -1)
arr = arr.transpose(0,2,1)

print(arr.shape)

h5f = h5py.File(output, 'w')
h5f.create_dataset('dataset_1', data = arr)
# arr = 3* np.random.rand(200,960,686)
'''n, m = arr.shape
num_shells = int(m/3)
shells_coords = np.array(np.hsplit(arr, num_shells))
print(shells_coords.shape)'''

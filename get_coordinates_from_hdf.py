import pandas as pd
import tables
import numpy as np
import h5py
import argparse
import json

def get_coordinates(filename: str, threshold: int=5):
    f = h5py.File(filename,'r')
    m = f['MDF']
    #PRINT(f.keys())
    dataset = m['images']['0']['image']
    arr = np.array(dataset)

    arr = arr.reshape(352,-1)
    df = pd.DataFrame(arr)
    non_zero_indices = df[df>thresh].stack().index.tolist()
    non_zero_coords = []
    for value in non_zero_indices:
        z = value[0]
        y = value[1] // 686
        x = value[1] - y * 686
        non_zero_coords.append((x,y,z))
    
    return non_zero_coords

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-f","--filename", type = str, help="name of the segmentation with h5 extension", required = True)
    parser.add_argument("-t","--threshold", type = int, help="threshold of color intensity, e.g.5", required = True)
   
    args = parser.parse_args()

    filename = args.filename
    thresh = args.threshold

f = h5py.File(filename,'r')
m = f['MDF']
#PRINT(f.keys())
dataset = m['images']['0']['image']
arr = np.array(dataset)

arr = arr.reshape(352,-1)
df = pd.DataFrame(arr)
non_zero_indices = df[df>thresh].stack().index.tolist()
non_zero_coords = []
for value in non_zero_indices:
	z = value[0]
	y = value[1] // 686
	x = value[1] - y * 686
	non_zero_coords.append((x,y,z))


jsonString = json.dumps(non_zero_coords)
jsonFile = open("coords.json","w")
jsonFile.write(jsonString)
jsonFile.close()


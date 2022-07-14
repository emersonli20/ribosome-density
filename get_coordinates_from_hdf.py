import pandas as pd
import numpy as np
import h5py
import argparse
import json
import os

def get_coordinates(filename: str, z: int, threshold: float=5):
    f = h5py.File(filename,'r')
    m = f['MDF']
    #PRINT(f.keys())
    dataset = m['images']['0']['image']  # type: ignore
    arr = np.array(dataset)

    arr = arr.reshape(z,-1)
    df = pd.DataFrame(arr)
    membrane_indices = df[df>threshold].stack().index.tolist()
    membrane_coords = []
    for value in membrane_indices:
        z = value[0]
        y = value[1] // 686
        x = value[1] - y * 686
        membrane_coords.append((x,y,z))
    
    return membrane_coords

def list_to_csv(membrane_coords, filename):
    os.makedirs("membrane_coords", exist_ok=True)
    new_filename = filename[:-3] + "csv"
    np.savetxt("membrane_coords/{}".format(new_filename), membrane_coords, delimiter=",")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-f","--filename", type=str, help="name of the segmentation with h5 extension", required = True)
    parser.add_argument("-t","--threshold", type=float, help="threshold of color intensity, e.g.5", required = True)
    parser.add_argument("-z","--z_range", type=int, help="z range of the tomogram", required = True)
    args = parser.parse_args()

    filename = args.filename
    threshold = args.threshold
    z = args.z_range
    membrane_coords = get_coordinates(filename, z, threshold)

    list_to_csv(membrane_coords, threshold)
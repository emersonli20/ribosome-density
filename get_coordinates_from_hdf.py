import pandas as pd
import numpy as np
import h5py
import argparse
import json

def get_coordinates(filename: str, z: int, threshold: float=5):
    f = h5py.File(filename,'r')
    m = f['MDF']
    #PRINT(f.keys())
    dataset = m['images']['0']['image']  # type: ignore
    arr = np.array(dataset)

    arr = arr.reshape(z,-1)
    df = pd.DataFrame(arr)
    non_zero_indices = df[df>threshold].stack().index.tolist()
    non_zero_coords = []
    for value in non_zero_indices:
        z = value[0]
        y = value[1] // 686
        x = value[1] - y * 686
        non_zero_coords.append((x,y,z))
    
    return non_zero_coords

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-f","--filename", type=str, help="name of the segmentation with h5 extension", required = True)
    parser.add_argument("-t","--threshold", type=float, help="threshold of color intensity, e.g.5", required = True)
    parser.add_argument("-z","--z_range", type=int, help="z range of the tomogram", required = True)
    args = parser.parse_args()

    filename = args.filename
    threshold = args.threshold
    z = args.z_range

    # f = h5py.File(filename,'r')
    # m = f['MDF']
    # #PRINT(f.keys())
    # dataset = m['images']['0']['image']
    # arr = np.array(dataset)

    # arr = arr.reshape(z,-1)
    # df = pd.DataFrame(arr)
    # non_zero_indices = df[df>threshold].stack().index.tolist()
    # non_zero_coords = []
    # for value in non_zero_indices:
    #     z = value[0]
    #     y = value[1] // 686
    #     x = value[1] - y * 686
    #     non_zero_coords.append((x,y,z))

    non_zero_coords = get_coordinates(filename, z, threshold)

    jsonString = json.dumps(non_zero_coords)
    jsonFile = open("coords.json","w")
    jsonFile.write(jsonString)
    jsonFile.close()
import ribosome_density
import numpy as np
import pandas as pd
import argparse
import timeit
import matplotlib.pyplot as plt
from tqdm import tqdm

if __name__ == "__main__":
    start = timeit.default_timer()
    parser = argparse.ArgumentParser()

    parser.add_argument("--tomogram", help="The name of the tomogram, contains ribosome data; e.g., 5913-2_L2_ts003", type=str, required=True)
    parser.add_argument("--radius", help="The radius of the sphere", type=float, required=True)
    parser.add_argument("-s", "--shell_coordinates", help="The csv file containing shell coordinates", type=str, required=True)
    parser.add_argument("-o", "--output", help="The name of the output csv file containing shell densities (include .csv in it)", type=str, required=True)

    args = parser.parse_args()

    tomogram = args.tomogram
    radius = args.radius
    shell_coordinates = args.shell_coordinates
    output = args.output

    print("Before getting coordinates")
    # get ribosome coordinates
    ribosome_coordinates = ribosome_density.get_coordinates(tomogram)
    print("After getting coordinates")

    # shells_coords: shape is (# points per shell, 3 * # shells)
    shells_coords_input = np.loadtxt(shell_coordinates, delimiter=",")
    n, m = shells_coords_input.shape

    num_shells = int(m/3)

    shells_coords = np.array(np.hsplit(shells_coords_input, num_shells))
    
    avg_densities = []

    print("Before getting avg_densities")
    
    for i in tqdm(range(num_shells)):
#         print("Shell {}".format(i))
        shell = list(map(tuple, shells_coords[i]))
        shell_density = ribosome_density.average_density(shell, ribosome_coordinates, radius)
        avg_densities.append(shell_density)
#         print(avg_densities)
        
    print("After getting avg_densities")

    print(avg_densities)
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    #save densities to csv file 
    arr = np.array(avg_densities);
    np.savetxt(output, arr, delimiter =',');
import ribosome_density
import numpy as np
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--tomogram", help="The name of the tomogram, contains ribosome data; e.g., 5913-2_L2_ts003", type=str, required=True)
    parser.add_argument("--radius", help="The radius of the sphere", type=float, required=True)

    args = parser.parse_args()

    tomogram = args.tomogram
    radius = args.radius

    # get ribosome coordinates
    coordinates = ribosome_density.get_coordinates(tomogram)

    # shells_coords: shape is (# points per shell, 3 * # shells)
    shells_coords_input = np.loadtxt("shells_coords.csv", delimiter=",")
    n, m = shells_coords_input.shape
    num_shells = int(m/3)

    shells_coords = np.array(np.hsplit(shells_coords_input, num_shells))
    
    avg_densities = []

    for i in range(num_shells):
        shell = list(map(tuple, shells_coords[i]))
        shell_density = ribosome_density.average_density(shell, coordinates, radius)
        avg_densities.append(shell_density)

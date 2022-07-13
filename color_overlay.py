import ribosome_density
import numpy as np
import argparse
import timeit
import matplotlib.pyplot as plt

if __name__ == "__main__":
    start = timeit.default_timer()
    parser = argparse.ArgumentParser()

    parser.add_argument("--tomogram", help="The name of the tomogram, contains ribosome data; e.g., 5913-2_L2_ts003", type=str, required=True)
    parser.add_argument("--radius", help="The radius of the sphere", type=float, required=True)

    args = parser.parse_args()

    tomogram = args.tomogram
    radius = args.radius

    # get ribosome coordinates
    ribosome_coordinates = ribosome_density.get_coordinates(tomogram)

    x = np.arange(-343,343,1, dtype = int);
    y = np.arange(-480,480,1, dtype = int);
    d = np.zeros((960,686));

    #for slice z=150
    for i in x:
        print(i)
        for j in y:
            d[j+480,i+343] = ribosome_density.get_density((i,j,150), ribosome_coordinates, radius)

    fig, ax = plt.subplots()
    im = ax.pcolormesh(x,y,d)
    fig.colorbar(im)
    plt.gca().set_aspect('equal')
    plt.savefig('/datadisk/cmholab3/tomography/first_slice.png')

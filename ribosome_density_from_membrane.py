import json
import matplotlib.pyplot as plt
import numpy as np
import numpy.ma as ma
import argparse

def get_coordinates(filename: str) -> list[tuple[float, float, float],...]:
    coordinates = []
    with open(filename) as f:
        data = json.load(f)
    
    for point in data["boxes_3d"]:
        coordinate = [point[0], point[1], point[2]]
        coordinates.append(coordinate)

    return coordinates

def graph_projection(coordinates: np.array, middle: int=150, interval: int=20):
    x = coordinates[:,0]
    y = coordinates[:,1]
    z = coordinates[:,2]

    lower = middle - interval
    upper = middle + interval

    condition = (z>lower) & (z<upper)
    projection = coordinates[condition]
    x_projection = projection[:, 0]
    y_projection = projection[:, 1]
    plt.scatter(x_projection,y_projection)
    plt.title("Membrane Projection")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def graph_3d(x: np.array, y: np.array, z: np.array):
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.scatter3D(x, y, z, s=10)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.title("Membrane 3d")
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-p","--projection", help="Display projection of tomogram onto the yz plane", action="store_true")
    parser.add_argument("--filename", help="Name of the json file containing the membrane coordinates", type=str, required=True)
    parser.add_argument("--middle_slice", help="Middle slice when looking at projection", type=int, default=150)
    parser.add_argument("--interval", help="Interval distance from middle slice when looking at projection", type=int, default=20)

    args = parser.parse_args()

    projection = args.projection
    filename = args.filename
    middle_slice = args.middle_slice
    interval = args.interval

    coordinate_list = get_coordinates(filename)
    coordinates_np = np.array(coordinate_list)

    theta = coordinates_np[:, 2]
    d1 = coordinates_np[:, 0] - 341 * np.sin(np.deg2rad(theta))
    d2 = coordinates_np[:, 1] - 480

    z = d1 * np.cos(np.deg2rad(theta))
    x = d1 * np.sin(np.deg2rad(theta))
    y = d2

    cartesian_coordinates = np.hstack([x[:,None],y[:,None],z[:,None]])

    if (projection):
        graph_projection(cartesian_coordinates, middle_slice, interval)
    else:
        graph_3d(x,y,z)


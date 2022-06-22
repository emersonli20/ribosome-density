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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-p","--projection", help="Display projection of tomogram onto the yz plane", type=bool)
    parser.add_argument("--filename", help="Name of the json file containing the membrane coordinates", type=str, required=True)
    args = parser.parse_args()

    projection = args.projection
    filename = args.filename

    coordinate_list = get_coordinates(filename)
    coordinates_np = np.array(coordinate_list)

    d1 = coordinates_np[:, 0]
    d2 = coordinates_np[:, 1]
    theta = coordinates_np[:, 2]

    x = d1 * np.cos(np.deg2rad(theta))
    y = d1 * np.sin(np.deg2rad(theta))
    z = d2

    if (projection):
        condition = (z>70) & (z<130)
        projection = coordinates_np[condition]
        condition = (z>70) & (z<130)
        projection = coordinates_np[condition]
        x_projection = projection[:, 0]
        y_projection = projection[:, 1]
        plt.scatter(x_projection,y_projection)
    else:
        fig = plt.figure()
        ax = plt.axes(projection="3d")
        ax.scatter3D(x, y, z, s=10)

    plt.show()
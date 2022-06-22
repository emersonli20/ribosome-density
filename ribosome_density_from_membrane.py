import json
import matplotlib.pyplot as plt
import numpy as np
import numpy.ma as ma

def get_coordinates(filename: str) -> list[tuple[float, float, float],...]:
    coordinates = []
    with open(filename) as f:
        data = json.load(f)
    
    for point in data["boxes_3d"]:
        coordinate = [point[0], point[1], point[2]]
        coordinates.append(coordinate)

    return coordinates

if __name__ == "__main__":
    coordinate_list = get_coordinates("ts_001_AreTomo_SART_reconstruction_TiltCor18_refineFlag1_VolZ1800_info_tmp.json")
    coordinates_np = np.array(coordinate_list)

    x = coordinates_np[:, 0]
    y = coordinates_np[:, 1]
    z = coordinates_np[:, 2]


    condition = (z>70) & (z<130)
    projection = coordinates_np[condition]

    print(projection.shape)
    # fig = plt.figure()
    # ax = plt.axes(projection="3d")

    x_projection = projection[:, 0]
    y_projection = projection[:, 1]
    plt.scatter(x_projection,y_projection)
    # ax.scatter3D(x, y, z, s=10)

    plt.show()
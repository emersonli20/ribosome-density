import math
from numpy.linalg import norm
from numpy import subtract
import numpy as np
import argparse
import json
import timeit

def get_coordinates(tomogram: str): #-> list[tuple[float, float, float]]:
    list_of_coordinates = []
    x = 0
    y = 0
    z = 0
    with open("run_data.star") as f:
        lines = f.readlines()
        for line in lines:
            words = line.split(" ")
            while ("" in words):
                words.remove("")         
            if tomogram in line:
                x = eval(words[0]) - 341
                y = eval(words[1]) - 480
                z = eval(words[2])
                list_of_coordinates.append((x,y,z))
        f.close()
    return list_of_coordinates

# def get_coordinates_json(filename: str):
#     coordinates = []
#     with open(filename) as f:
#         data = json.load(f)

#     for point in data["boxes_3d"]:
#         coordinate = (point[0], point[1], point[2])
#         coordinates.append(coordinate)

#     return coordinates

def get_distance(c1, c2): # -> np.floating:
    return norm(subtract(c1, c2))

def get_density(point_of_interest, list_of_coordinates, threshold: float): #-> tuple[int, dict[tuple[float,float,float], int]]:
    distances = {}
    for c1 in list_of_coordinates:
        distance = get_distance(c1, point_of_interest)
        if distance <= threshold:
            distances[c1] = distance
    return len(distances)
    
def average_density(points_of_interest, list_of_coordinates, threshold: float): # -> float:
    n = len(points_of_interest)
    avg_density = 0.0;
    for i, point in enumerate(points_of_interest):
        #print("Point {}".format(i))
        avg_density += get_density(point, list_of_coordinates, threshold) / n
    
    return avg_density

def get_all_densities(points_of_interest, list_of_coordinates, threshold: float): #-> list[float]:
    all_densities = [];
    for i, point in enumerate(points_of_interest):
        all_densities.append(get_density(point, list_of_coordinates, threshold))

    return all_densities

if __name__ == "__main__":
    start = timeit.default_timer()
    parser = argparse.ArgumentParser()

    parser.add_argument("--tomogram", help="The name of the tomogram; e.g., 5913-2_L2_ts003", type=str, required=True)
    parser.add_argument("--x", help="The x coordinate of the point", type=float, required=True)
    parser.add_argument("--y", help="The y coordinate of the point", type=float, required=True)
    parser.add_argument("--z", help="The z coordinate of the point", type=float, required=True)
    parser.add_argument("--radius", help="The radius of the sphere", type=float, required=True)
    
    args = parser.parse_args()

    tomogram = args.tomogram
    x = args.x
    y = args.y
    z = args.z
    radius = args.radius

    point_of_interest = (x,y,z)

    coordinates = get_coordinates(tomogram)
    counter, distances = get_density(point_of_interest, coordinates, radius)
    print("counter: {}\n".format(counter))
    print("distances: {}\n".format(distances))

    stop = timeit.default_timer()

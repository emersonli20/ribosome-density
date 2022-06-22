import math
from numpy.linalg import norm
from numpy import subtract
import argparse

def get_coordinates(tomogram: str) -> list[tuple[float, float, float], ...]:
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
                x = eval(words[0])
                y = eval(words[1])
                z = eval(words[2])
                list_of_coordinates.append((x,y,z))
        f.close()
    return list_of_coordinates

def get_distance(c1: tuple[float, float, float], c2: tuple[float, float, float]) -> float:
    return norm(subtract(c1, c2))

def get_density(list_of_coordinates: list[tuple[float, float, float], ...], c2: tuple[float, float, float], threshold: float) -> (int, list[float, ...]):
    distances = {}
    for c1 in list_of_coordinates:
        distance = get_distance(c1, c2)
        if distance <= threshold:
            distances[c1] = distance
    return len(distances), distances
    
if __name__ == "__main__":
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

    c2 = (x,y,z)

    coordinates = get_coordinates(tomogram)
    counter, distances = get_density(coordinates, c2, radius)
    print("counter: {}\n".format(counter))
    print("distances: {}\n".format(distances))
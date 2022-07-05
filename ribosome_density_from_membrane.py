import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import argparse

def load_membrane_data(membrane_data_filename: str) -> np.ndarray:
    """
    Loads coefficients of best fit curves for every z slice
    Arguments:
        membrane_data_filename: str representing the csv input file containing membrane best fit curves
    Returns:
        membrane_data: np.ndarray of shape (z,m), type float
            z: number of best fit curves in the xy-plane (1 for each slice)
            m: number of coefficients 
    """

    membrane_data = np.genfromtxt(membrane_data_filename)

    return membrane_data

def min_distance(point: np.ndarray, membrane_data: np.ndarray) -> float:
    # calcuate the distance equation from point to each best fit curve function
    z, m = membrane_data.shape
    distance_equations = []
    x = Symbol('x')
    for i, curve in range(membrane_data.shape[0]):
        coefficients = {}
        # i corresponds to the degree of each coefficient in the polynomial
        coefficients[i] = curve[m-1-i]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--membrane_data_filename", type=str, required=True)

    args = parser.parse_args()
    
    membrane_data_filename = args.membrane_data_filename

import pandas as pd
from matplotlib import pyplot as plt
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-f", "--filename", help="Csv file containing densities to graph (include .csv)", required=True, type=str)
    parser.add_argument("-o", "--output", help="File path of the output (include .png)", required=True, type=str)

    args = parser.parse_args()

    filename = args.filename
    output = args.output

    #plot density wrt distance from membrane
    df = pd.read_csv(filename, sep=',', header=None);
    df.plot()
    plt.savefig(output)
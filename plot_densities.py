import pandas as pd
from matplotlib import pyplot as plt
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-f", "--filename", help="Csv file containing densities to graph (include .csv)", required=True, type=str)
    parser.add_argument("-t", "--membrane_type", help="pm, pvm, or dv", required=True, type=str)

    args = parser.parse_args()

    filename = args.filename
    membrane_type = args.membrane_type

    #plot density wrt distance from membrane
    df = pd.read_csv(filename, sep=',', header=None);
    df.plot()
    plt.savefig('{}_plot.png'.format(membrane_type))
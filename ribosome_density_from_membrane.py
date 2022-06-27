import json
import matplotlib.pyplot as plt
import numpy as np
import numpy.ma as ma
import argparse
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import get_coordinates_from_hdf

def get_coordinates(filename: str, threshold: int=5):
    coordinates = get_coordinates_from_hdf.get_coordinates(filename, threshold)

    return coordinates

def graph_projection(coordinates: np.array, middle: int=150, interval: int=20):
    x = coordinates[:,0]
    y = coordinates[:,1]
    z = coordinates[:,2]

    lower = middle - interval
    upper = middle + interval

    z_condition = (z>=lower) & (z<=upper)
    projection = coordinates[z_condition]
    # print(projection)
    x_projection = projection[:, 0]
    y_projection = projection[:, 1]

    # colors = ['b','g','r','c','m','y','b','g','r','c','m''b','g','r','c','m','y','b','g','r','c','m','b','g','r','c','m','y','b','g','r','c','m','b','g','r','c','m','y','b','g','r','c','m','b','g','r','c','m','y','b','g','r','c','m''b','g','r','c','m','y','b','g','r','c','m','b','g','r','c','m','y','b','g','r','c','m','b','g','r','c','m','y','b','g','r','c','m']
    # residuals = []
    # thetas ={}
    # i = 0
    # for x_lower in [-300,-250,-200,-150,-100,-50,0,50,100,150,200]:
    #     for interval in [100, 150, 200, 250]:
    #         print(i)
    #         x_upper = x_lower + interval
    #         color = colors[i]
    #         print(x_lower)
    #         x_condition = (x_projection>=x_lower) & (x_projection<=x_upper)
    #         print(x_condition)
    #         x_slice = projection[x_condition]
            
    #         x_fit = x_slice[:,0]
    #         # print(x_fit)
    #         y_fit = x_slice[:,1]

    #         print(y_fit)
    #         print(x_fit)

    #         # horizontal-opening parabola
    #         theta,res,_,_,_ = np.polyfit(y_fit, x_fit, 2, full=True)
    #         print("mse: {}".format(res))
    #         residuals.append(res)
    #         thetas[i] = theta

    #         i += 1
        
    # print("residuals: {}".format(residuals))
    # residuals = [a[0] for a in residuals]
    # print("residuals: {}".format(residuals))
    # best_indices = np.argsort(residuals)[::-1][:2]
    # print(best_indices)
    # best_thetas = [thetas.get(i) for i in best_indices]

    # for j,theta in enumerate(best_thetas):
    #     f = np.poly1d(theta)
    #     color = colors[j]
    #     # x_line = theta[2] + theta[1] * pow(y_fit, 1) + theta[0] * pow(y_fit, 2)
    #     for y1 in np.linspace(-500,500,1000):
    #         plt.plot(f(y1), y1, 'o{}'.format(color))

    # plt.plot(x_line, y_range, 'r')

    # vertical-opening parabola
    # theta = np.polyfit(x_fit, y_fit, 2)
    # print(theta)
    # y_line = theta[2] + theta[1] * pow(x_fit, 1) + theta[0] * pow(x_fit, 2)
    # plt.plot(x_fit, y_line, 'r')

    plt.xlim(-300,300)
    plt.ylim(-500,500)
    plt.scatter(x_projection,y_projection)
    plt.title("Membrane Projection")
    plt.xlabel("x")
    plt.ylabel("y")
    txt = "Slices: [{}, {}]".format(lower, upper)
    plt.figtext(0.5,0.01, txt)
    plt.show()

def graph_3d_slice(coordinates: np.array, middle: int=150, interval: int=20):
    x = coordinates[:,0]
    y = coordinates[:,1]
    z = coordinates[:,2]

    lower = middle - interval
    upper = middle + interval

    condition = (z>=lower) & (z<=upper)
    projection = coordinates[condition]
    x_projection = projection[:, 0]
    y_projection = projection[:, 1]
    z = projection[:,2]
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.scatter3D(x_projection, y_projection, z, s=10)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    set_axes_equal(ax)
    plt.title("Membrane 3d")
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

def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-p","--projection", help="Display projection of tomogram onto the xy plane", action="store_true")
    parser.add_argument("-s","--slice_3d", help="Display slice along z-axis in 3d", action="store_true")
    parser.add_argument("--filename", help="Name of the hdf file containing the membrane coordinates", type=str, required=True)
    parser.add_argument("--middle_slice", help="Middle slice when looking at projection", type=int, default=150)
    parser.add_argument("--interval", help="Interval distance from middle slice when looking at projection", type=int, default=20)
    parser.add_argument("-t","--threshold", type = int, help="threshold of color intensity, e.g.5", required = True)

    args = parser.parse_args()

    projection = args.projection
    filename = args.filename
    middle_slice = args.middle_slice
    interval = args.interval
    slice_3d = args.slice_3d
    thresh = args.threshold

    coordinate_list = get_coordinates(filename, thresh)
    coordinates_np = np.array(coordinate_list)

    x = coordinates_np[:, 0] - 341
    y = coordinates_np[:, 1] - 480
    z = coordinates_np[:, 2]
  
    cartesian_coordinates = np.hstack([x[:,None],y[:,None],z[:,None]])

    if (projection):
        graph_projection(cartesian_coordinates, middle_slice, interval)
    elif (slice_3d):
        graph_3d_slice(cartesian_coordinates, middle_slice, interval)
    else:
        graph_3d(x,y,z)


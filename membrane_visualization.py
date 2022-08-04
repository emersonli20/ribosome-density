import json
import matplotlib.pyplot as plt
import numpy as np
import numpy.ma as ma
import argparse
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import get_coordinates_from_hdf

def membrane_distances(coordinates: np.ndarray):
    # TODO: find the subtracted matrix
    subtracted = coordinates

    slices = []
    for i in range(0,3*n,3):
        sliced = subtracted[:,i:i+3]
        norm = np.linalg.norm(sliced,axis=1)
        slices.append(norm)
    print(len(slices))
    distances = np.array(slices)
    
    return distances

def distance_filter(distances: np.ndarray, radius: float, threshold = float):
    distances[distances > radius] = 0
    count_matrix = np.count_nonzero(distances, axis=0)
    boolean_array = count_matrix > threshold
    return boolean_array
    

def get_coordinates_json(filename: str):
    coordinates = []
    with open(filename) as f:
        data = json.load(f)

    for point in data["boxes_3d"]:
        coordinate = (point[0], point[1], point[2])
        coordinates.append(coordinate)

    return coordinates

def get_coordinates(filename: str, threshold: float=5):
    coordinates = get_coordinates_from_hdf.get_coordinates(filename, threshold)

    return coordinates

def graph_projection(coordinates: np.ndarray, coordinates_discard: np.ndarray, middle: int=150, interval: int=20):
    x = coordinates[:,0]
    y = coordinates[:,1]
    z = coordinates[:,2]
    z_discard = coordinates_discard[:,2]

    lower = middle - interval
    upper = middle + interval

    z_condition = (z>=lower) & (z<=upper)
    z_discard_condition = (z_discard>=lower) & (z_discard<=upper)
    projection = coordinates[z_condition]
    discard_projection = coordinates_discard[z_discard_condition]
    # print(projection)
    x_projection = projection[:, 0]
    y_projection = projection[:, 1]
    x_discard_projection = discard_projection[:,0]
    y_discard_projection = discard_projection[:,1]

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
    plt.scatter(x_projection,y_projection, s=5, c='b')
    plt.scatter(x_discard_projection, y_discard_projection, s=5, c='r')
    plt.title("Membrane Projection")
    plt.xlabel("x")
    plt.ylabel("y")
    txt = "Slices: [{}, {}]".format(lower, upper)
    plt.figtext(0.5,0.01, txt)
    plt.show()

def graph_3d_slice(coordinates: np.ndarray, coordinates_discard : np.ndarray, middle: int=150, interval: int=20):
    x = coordinates[:,0]
    y = coordinates[:,1]
    z = coordinates[:,2]
    x_discard = coordinates_discard[:,0]
    y_discard = coordinates_discard[:,1]
    z_discard = coordinates_discard[:,2]

    lower = middle - interval
    upper = middle + interval

    condition = (z>=lower) & (z<=upper)
    projection = coordinates[condition]
    discard_projection = coordinates_discard[condition]
    x_projection = projection[:, 0]
    y_projection = projection[:, 1]

    x_discard_projection = discard_projection[:,0]
    y_discard_projection = discard_projection[:,1]

    z = projection[:,2]
    fig = plt.figure()
    plt.xlim(-300,300)
    plt.ylim(-500,500)
    ax = plt.axes(projection="3d")
    ax.scatter3D(x_projection, y_projection, z, s=5, c='b')
    ax.scatter3D(x_discard_projection, y_discard_projection, z, s=5, c='r')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    set_axes_equal(ax)
    plt.title("Membrane 3d")
    plt.show()

def graph_3d(x: np.ndarray, y: np.ndarray, z: np.ndarray, x_discard: np.ndarray, y_discard: np.ndarray, z_discard: np.ndarray):
    fig = plt.figure()
    plt.xlim(-300,300)
    plt.ylim(-500,500)
    ax = plt.axes(projection="3d")
    ax.scatter3D(x, y, z, s=5, c='b')
    ax.scatter3D(x_discard, y_discard, z_discard, s=5, c='r')
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
    parser.add_argument("--filename", help="Name of the hdf file containing the membrane coordinates", type=str)
    parser.add_argument("--filename_json", help="Name of the json file containing the membrane coordinates", type=str)
    parser.add_argument("--middle_slice", help="Middle slice when looking at projection", type=int, default=150)
    parser.add_argument("--interval", help="Interval distance from middle slice when looking at projection", type=int, default=20)
    parser.add_argument("-t","--threshold", type=float, help="threshold of color intensity, e.g.5", required = True)
    parser.add_argument("-r","--radius", type=float, help="radius for denoising threshold", required = True)
    parser.add_argument("-d","--denoise_threshold", type=float, help="denoise threshold; i.e., number of particles within radius", required=True)


    args = parser.parse_args()

    projection = args.projection
    filename = args.filename
    filename_json = args.filename_json
    middle_slice = args.middle_slice
    interval = args.interval
    slice_3d = args.slice_3d
    threshold = args.threshold
    radius = args.radius
    denoise_threshold = args.denoise_threshold

    # coordinate_list = get_coordinates(filename, threshold)

    coordinate_list = get_coordinates(filename, threshold)
    n = len(coordinate_list)
    #print(n)

    coordinates_np = np.array(coordinate_list)
    #dtype= "i,i,i")

    mat_1 = np.tile(coordinates_np, n)
    mat_2 = coordinates_np.reshape((1,n*3),order='C');
    mat_2 = np.tile(mat_2, (n,1))
    mat_diff = np.subtract(mat_1, mat_2)


    # TODO: pass subtracted matrix into membrane_distances
    distances = membrane_distances(mat_diff)

  
    # cartesian_coordinates = np.hstack([x[:,None],y[:,None],z[:,None]])

    boolean_array = distance_filter(distances, radius, denoise_threshold)
    coordinates_filtered = coordinates_np[boolean_array, :]
    discarded = coordinates_np[np.logical_not(boolean_array), :]

    x = coordinates_filtered[:, 0] - 341
    y = coordinates_filtered[:, 1] - 480
    z = coordinates_filtered[:, 2]
  
    x_discard = discarded[:, 0] - 341
    y_discard = discarded[:, 1] - 480
    z_discard = discarded[:, 2]
    coordinates = np.hstack([x[:,None],y[:,None],z[:,None]])
    coordinates_discard = np.hstack([x_discard[:,None],y_discard[:,None],z_discard[:,None]])

    if (projection):
        graph_projection(coordinates, coordinates_discard, middle_slice, interval)
    elif (slice_3d):
        graph_3d_slice(coordinates, coordinates_discard, middle_slice, interval)
    else:
        graph_3d(x,y,z,x_discard, y_discard, z_discard)

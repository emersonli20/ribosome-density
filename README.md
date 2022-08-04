# ribosome-density
## Install Dependencies
```
pip install -r requirements.txt
```
## ribosome_density.py
To view usage instructions:
```
python ribosome_density.py --help
```
* Input the name of the tomogram, must have star file in directory
* Input an x, y, z coordinate in angstroms
* Input a radius in angstroms
* Outputs the number of ribosomes within the given radius of the given coordinate

## membrane_visualization.py
To view usage instructions:
```
python membrane_visualization --help
```
* Given a json file with membrane coordinates (acquired via eman2)
* Graph the membrane coordinates
  * Graph in 3d
  * Graph slice in 3d with respect to z-axis
  * Graph projection onto xy plane
  
## compute_average_densities.py
To view usage instructions:
```
python compute_average_densities.py --help
```
* Input the name of the tomogram, must have star file in directory
* Input a csv file containing membrane coordinates, obtained from Matlab

## Examples
### 3d Membrane Example
![3d Membrane Example](https://github.com/emersonli20/ribosome-density/blob/master/3d_membrane.png)

### 2d Membrane Example with Best Fit Lines
<p align="center">
 <img src="https://github.com/emersonli20/ribosome-density/blob/master/2d_membrane_best_fit_lines.png" alt="2d Membrane Example with Best Fit Lines" height=400 class="center">
</p>

## ribosome_density_from_membrane.py
To view usage instructions:
```
python ribosome_density_from_membrane.py --help
```
### Plot of Ribosome Density as a Function of Distance From Membrane (5970_L5_ts001)
<p align="center">
 <img src="https://github.com/emersonli20/ribosome-density/blob/master/5970_L5_ts001_densities_plot.png" alt="Ribosome density plot of 5970_L5_ts001" height=400 class="center">
</p>

## Convert HDF to CSV

* run 3dmod on the desired tomogram to see what the z-range is
```
3dmod [path_to_tomogram]
```
* run get_coordinates_from_hdf.py with threshold 1 and the z-range you've just obtained
```
python3 get_coordinates_from_hdf.py -f [path_to_tomogram] -t 1 -z [z-range from 3dmod]
```

## Select Desired Membranes on MATLAB

* open brushing.m
* uncomment the first line, and change the path to the csv file of all the coordinates from the hdf
* run brushing.m and click on the brushing tool in the figure, and select the membranes you want
* go to tools-> brushing-> export brushed -> OK (do not need to change the variable name)
* uncomment the last line, and change the path to the name of the csv file you want to create for the selected membrane; the coordinates of the selected membrane should be saved in that csv file.
* ***remember to eyeball the shell_number! 1/10 of the distance from membrane to the border of the tomogram, round up if unsure***

## Create Equidistant Shells of Membranes
* open equidistant_shells_from_csv.m
* uncomment the first line and change the path to the output file from brushing.m
* change the parameters accordingly: 
     - compress_ratio: the higher the ratio, the fewer points reduce the number of points used on the membrane
     - neighbors: number of nearest neighbors used for estimating the normals
     - ***shell_number***: number of shells wanted (default shell stepsize is 10)
* run the entire file
* afterwards, type and run this in the COMMAND WINDOW:
```show_normals(ptcloud, adjusted_normals) ```
     - eyeball the coordinates for a sensorCenter to which the normals should be oriented
     - go back to equidistant_shells_from_csv.m and change the sensorCenter coordinates accordingly in line 13
* check central slice image on benchling:
     - if the membrane is relatively horizontal, uncomment line 20
     - if you want to save adjusted_normals to csv, uncomment line 22
* run the entire equidistant_shells_from_csv.m file, and the output should be a csv called 'pm/pvm/dv_shells_coords_%shell_number.csv'

## getting the average densities csv and line plot
* run this in the folder of the segmentations of the particular tilt series of interest:
```
python3 /*insert path/compute_average_densities.py --tomogram *insert tomogram, e.g. 5970_L5_ts001* --radius *insert radius of sphere* -m *insert pm/pvm/dv_shells_coords*.csv -mt *insert pv/pvm/dv*
```
## Membrane Segmentation using Matlab Brushing
### 1. Brushing
* If you only have an hdf file of the segmentation, use **get_coordinates_from_hdf.py** to convert it to a csv file
* Open **brushing.m**
* Uncomment the "load prebrushed coordinates" section and the "plot and write coordinates" section, and comment the "load postbrushed coordinates section"
* Load your csv file of unbrushed coordinates (from **get_coordinates_from_hdf.py**; shape n x 3)
```
pre_brushed = csvread("[name of your unbrushed coordinates file]")
```
* In the last line of **brushing.m**, set the path of your output from the brushing, as well as the name of the brushed data variable in the matlab
```
csvwrite("[output path for csv]",[name of brushed data variable in matlab workspace])
```
* Run **brushing.m** from the matlab command prompt
* Use the brushing tool (explained above) to select your membrane and save in the matching brushed data variable
* Uncomment the "load postbrushed coordinates section" and comment everything else"
* Run **brushing.m** from the matlab command prompt again 

### 2. Curve Fitter: Fitting the Central Surface
* Use **curveFitter** tool from Matlab command window to fit a surface to x, y, and z point cloud data
* Determine which type of polynomial function best fits the data
* Export the fitted surface to workspace and name it "centralSurface"
### 3. Create the Central Surface Grid
* Open **membrane_grid.m**
* In the "load coefficients" and "create grid" sections, unpack the surface coefficients according to what degree polynomial you used
* In the last line containing "csvwrite", set the name of your output csv containing your central grid coordinates
* Run **membrane_grid.m** from the matlab command prompt
### 4. Creating the Boundary Surface Grids
* Open **create_membrane_boundaries.m**
* In the 1st line, load your csv file containing the central membrane grid by setting the csvwrite argument
* In the last lines, set the output file name of the csv containing the coordinates of your boundary surface grids
* Run **create_membrane_boundaries.m** from the matlab command prompt
### 5. Curve Fitter: Fitting the Boundary Surfaces
* Open **plot_membrane_boundaries.m**
* Uncomment the load membrane grid section and comment everything else
* In the 1st line, load your csv file containing the boundary membrane grids by setting the csvwrite argument
* Run **plot_membrane_boundaries.m** from the matlab command prompt
* Run **curveFitter** from the matlab command line and fit surface1 and surface2 using (x1,y1,z1) and (x2,y2,z2) respectively
* Export surface1 and surface2 the workspace
### 6. Save Boundary Surface Coordinates
* Open **fill_membrane.m**
* Adjust the unpacked coefficients based on the degree of the polynomial you used for the surface fits
* Run **fill_membrane.m** from the matlab command prompt
### 7. Create Membrane Filling
* Open **fill_grid.py**
* Adjust the number of coefficients based on polynomial degree
* Set the output filenames
  * filled membrane file (used to convert to hdf)
  * indices file (used to visualize membrane in python/matlab)
* Run **fill_grid.py**
* Run **csv_to_hdf.py**, pass the x_dim (~686), output (.h5 file), and filename (filled membrane csv from fill_grid.py) as command line arguments
### 8.a. Matlab Visualization
* Open **plot_membrane_boundaries.m**
* Uncomment everything
* Run **plot_membrane_boundaries.m**
### 8.b. ChimeraX Visualization
```
chimerax [output .h5 file from csv_to_hdf.py]
```

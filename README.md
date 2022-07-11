# ribosome-density
## Install Dependencies
```
pip -r requirements.txt
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


## Select Desired Membranes on MATLAB

* open brushing.m
* uncomment the first line, and change the path to the csv file of all the coordinates from the hdf
* uncomment the last line, and change the path to the name of the csv file you want to create for the selected membrane
* run brushing.m and click on the brushing tool in the figure, and select the membranes you want
* go to tools-> brushing-> export brushed -> OK (do not need to change the variable name)
* the coordinates of the selected membrane should be saved in a csvfile in the previously specified path

## Create Equidistant Shells of Membranes
* open equidistant_shells_from_csv.m
* uncomment the first line and change the path to the output file from brushing.m
* change the parameters accordingly: 
     - compress_ratio: reduce the number of points used on the membrane
     - neighbors: number of nearest neighbors used for estimating the normals
     - shell_number: number of shells wanted
* run the matlab file, and the output should be a csv file called 'shells_coords_%shellnumber.csv'

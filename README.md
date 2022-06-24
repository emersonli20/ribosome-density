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
* Input an x, y, z coordinate in angstroms
* Input a radius in angstroms
* Outputs the number of ribosomes within the given radius of the given coordinate

## ribosome_density_from_membrane.py
To view usage instructions:
```
python ribosome_density_from_membrane.py --help
```
* Given a json file with membrane coordinates (acquired via eman2)
* Graph the membrane coordinates
  * Graph in 3d
  * Graph slice in 3d with respect to z-axis
  * Graph projection onto xy plane

## Examples
### 3d Membrane Example
![3d Membrane Example](https://github.com/emersonli20/ribosome-density/blob/master/3d_membrane.png)

### 2d Membrane Example with Best Fit Lines
<p align="center">
 <img src="https://github.com/emersonli20/ribosome-density/blob/master/2d_membrane_best_fit_lines.png" alt="2d Membrane Example with Best Fit Lines" height=400 class="center">
</p>

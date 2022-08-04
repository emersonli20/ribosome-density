mem = csvread("5991_L2_ts004_central_membrane_grid.csv");

% generate original pointcloud and normals
compress_ratio = 20;
neighbors = 20;

% mem_compressed = mem(1:compress_ratio:end, 1:3);
ptcloud = pointCloud(mem);
normals = pcnormals(ptcloud, neighbors);

%CHANGE sensorCenter accordingly
sensorCenter = [-300,400,125]; 

adjusted_normals = get_adjusted_normals(ptcloud, normals, sensorCenter);

n = numel(adjusted_normals)/3 %number of mem points selected

% OPTIONAL step, uncomment if needed: manually flip the rest of the upward-facing normals
% adjusted_normals = manually_flip_y(adjusted_normals);

% csvwrite("adjusted_normals.csv", adjusted_normals);

% generate shells, write to csv
stepsize = 3 % default shell stepsize = 10

shells = membrane_boundary_shells(mem, adjusted_normals, stepsize);

filename = sprintf('5991_L2_ts004_membrane_boundaries_6.csv')

csvwrite(filename,  shells);

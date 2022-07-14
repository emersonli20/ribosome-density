% variables to pass from command line
read_file = r;
write_file = w;

mem = csvread(read_file);

% generate original pointcloud and normals
compress_ratio = 20;
neighbors = 400;
shell_number = 200;

mem_compressed = mem(1:compress_ratio:end, 1:3);
ptcloud = pointCloud(mem_compressed);
normals = pcnormals(ptcloud, neighbors);

%CHANGE sensorCenter accordingly
sensorCenter = [-100,-200, 140]; 

adjusted_normals = get_adjusted_normals(ptcloud, normals, sensorCenter);

n = numel(adjusted_normals)/3 %number of mem points selected

% OPTIONAL step, uncomment if needed: manually flip the rest of the upward-facing normals
% adjusted_normals = manually_flip_y(adjusted_normals);

% csvwrite("adjusted_normals.csv", adjusted_normals);

% generate shells, write to csv
stepsize = 10 % default shell stepsize = 10
shells = make_shells(mem_compressed, adjusted_normals, shell_number, stepsize);
filename  = sprintf('%s%d.csv', write_file, shell_number)
csvwrite(filename,  shells);

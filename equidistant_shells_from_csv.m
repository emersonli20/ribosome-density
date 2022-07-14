mem = csvread("20220121_5970_L5_ts003/pm/pm.csv");

% generate original pointcloud and normals
compress_ratio = 20;
neighbors = 400;
shell_number = 80;

mem_compressed = mem(1:compress_ratio:end, 1:3);
ptcloud = pointCloud(mem_compressed);
normals = pcnormals(ptcloud, neighbors);

%CHANGE sensorCenter accordingly
sensorCenter = [350,100,150]; 

adjusted_normals = get_adjusted_normals(ptcloud, normals, sensorCenter);

n = numel(adjusted_normals)/3 %number of mem points selected

% OPTIONAL step, uncomment if needed: manually flip the rest of the upward-facing normals
adjusted_normals = manually_flip_y(adjusted_normals);

% csvwrite("adjusted_normals.csv", adjusted_normals);

% generate shells, write to csv
stepsize = 10 % default shell stepsize = 10
shells = make_shells(mem_compressed, adjusted_normals, shell_number, stepsize);
filename  = sprintf('20220121_5970_L5_ts003/pm/pm_shells_coords_%d.csv', shell_number)

csvwrite(filename,  shells);

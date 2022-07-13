% all_coords = csvread("coordinates_3.0.csv");
mem = csvread("/path of pv/pvm/dv membrane coords.csv");

% generate original pointcloud and normals
compress_ratio = 3
mem_compressed = mem(1:compress_ratio:end, 1:3);
ptcloud = pointCloud(mem_compressed);
normals = pcnormals(ptcloud, 400);
adjusted_normals = get_adjusted_normals(ptcloud, normals);
n = numel(adjusted_normals)/3 %number of mem points selected
% OPTIONAL step, uncomment if needed: manually flip the rest of the upward-facing normals
% adjusted_normals = manually_flip_y(adjusted_normals);
show_normals(ptcloud, adjusted_normals)
% csvwrite("adjusted_normals.csv", adjusted_normals);
% generate shells, write to csv
shell_number = 150
shells = make_shells(mem_compressed, adjusted_normals, shell_number);
filename  = sprintf('/path of output pm/pvm/dv_shells_coords_%d.csv',shell_number)
csvwrite(filename,  shells);

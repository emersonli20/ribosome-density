% all_coords = csvread("coordinates_3.0.csv");
mem = csvread("/datadisk/cmholab3/tomography/20220120_5970-3_trophs/L5/eman2/ts001/inner_mem_1_coords.csv");

% generate original pointcloud and normals
compress_ratio = 3
mem_compressed = mem(1:press_ratio:end, 1:3);
ptcloud = pointCloud(mem_compressed);
normals = pcnormals(ptcloud, 400);
adjusted_normals = get_adjusted_normals(ptcloud, normals);
n = numel(adjusted_normals)/3 %number of mem points selected
% manually flip the rest of the upward-facing normals
adjusted_normals = manually_flip_y(adjusted_normals);
show_normals(ptcloud, adjusted_normals)
% write final normals to csv
csvwrite("adjusted_normals.csv", adjusted_normals);
% generate shells, write to csv
shell_number = 150
shells = make_shells(mem, adjusted_normals, shell_number);
filename  = sprintf('shells_coords_%d.csv',shell_number)
csvwrite(filename,  shells);

% hold on
% pcshow(ptcloud);

% % visualization of shells
% shell_10 = shells(:,:,10);
% shell_20 = shells(:,:,20);
% shell_30 = shells(:,:,30);
% ptcloud_10 = pointCloud(shell_10);
% ptcloud_20 = pointCloud(shell_20);
% ptcloud_30 = pointCloud(shell_30);
% pcshow(ptcloud_10);
% pcshow(ptcloud_20);
% pcshow(ptcloud_30);
% xlabel('x')
% ylabel('y')
% zlabel('z')
% view([0,0,180])
% hold off
% 


% all_coords = csvread("coordinates_3.0.csv");
mem = csvread("inner_mem_coords.csv");

% generate original pointcloud and normals
ptcloud = pointCloud(mem);
normals = pcnormals(ptcloud, 120);
adjusted_normals = get_adjusted_normals(ptcloud, 5,120);
n = numel(adjusted_normals)/3

% manually flip the rest of the upward-facing normals
% adjusted_normals = manually_flip_y(adjusted_normals);
show_normals(ptcloud, 5, adjusted_normals)
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

% %all_coords = csvread("5991_L2_ts001_membrane_boundaries" + ".csv");
% pre_brushed = csvread("./membrane_coords/220105_5991-2_L2_ts004_preproc_low0.25__membranes_4.csv")
% x = pre_brushed(:,1)
% y = pre_brushed(:,2)
% z = pre_brushed(:,3)

all_coords = csvread('5991_L2_ts004_1.25.csv')
x = all_coords(:,1)
y = all_coords(:,2)
z = all_coords(:,3)



% filled_membrane = csvread("indices.csv")
% filled_membrane = reshape(filled_membrane, [256, 686, 960])
% filled_membrane = permute(filled_membrane, [0,2,1])

% size(filled_membrane)

% plot3(x, y, z,'.')
% hold on
% 
% x_filled = filled_membrane(:,1) - x_min
% y_filled = filled_membrane(:,2) - y_min
% z_filled = filled_membrane(:,3) - z_min

% plot3(x_filled,y_filled,z_filled)
% 
% xlabel('x')
% ylabel('y')
% zlabel('z')
% axis equal
% view([0,0,180])
% 
% hold off
% 
% % path = insert_desired_output_path_of_selected_membrane
% csvwrite("5991_L2_ts004_1.25.csv",brushedData125)

load prebrushed coordinates
pre_brushed = csvread("./membrane_coords/220105_5991-2_L2_ts004_preproc_low0.25__membranes_4.csv")
x = pre_brushed(:,1)
y = pre_brushed(:,2)
z = pre_brushed(:,3)

% plot and write coordinates
plot3(x, y, z,'.')
xlabel('x')
ylabel('y')
zlabel('z')
axis equal
view([0,0,180])
% % 
% % path = insert_desired_output_path_of_selected_membrane
csvwrite("5991_L2_ts004_1.25.csv",brushedData125)

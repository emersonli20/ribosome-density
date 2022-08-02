all_coords = csvread("membrane_coords/20220121_5970_L5_ts003_preproc_low0.25__good_mem_001_seg.csv");

plot3(all_coords(:,1), all_coords(:,2), all_coords(:,3),'.')

xlabel('x')
ylabel('y')
zlabel('z')

view([0,0,180])
axis equal

% path = insert_desired_output_path_of_selected_membrane

csvwrite("20220121_5970_L5_ts003/pm/pm.csv", pm_5970_L5_ts003)

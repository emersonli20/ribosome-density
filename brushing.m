% variables to pass from command line
read_file = r;
write_file = w;

all_coords = csvread(read_file);

plot3(all_coords(:,1), all_coords(:,2), all_coords(:,3),'.')

xlabel('x')
ylabel('y')
zlabel('z')

view([0,0,180])
axis equal

% path = insert_desired_output_path_of_selected_membrane

csvwrite(write_file, brushedData)

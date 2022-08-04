% load membrane boundary grid
membrane_boundaries = csvread("5991_L2_ts004_membrane_boundaries_6.csv")
x1 = membrane_boundaries(:,1)
y1 = membrane_boundaries(:,2)
z1 = membrane_boundaries(:,3)
x2 = membrane_boundaries(:,4)
y2 = membrane_boundaries(:,5)
z2 = membrane_boundaries(:,6)

% plot surfaces and fill
fill = csvread("indices.csv")
plot(surface1, [x1,y1], z1)
hold on
plot(surface2, [x2,y2], z2)
plot3(fill(:,1),fill(:,2),fill(:,3))


% plot3(fill(:,1)+x_min,fill(:,2)+y_min,fill(:,3)+z_min, ".")
% 
xlabel('x')
ylabel('y')
zlabel('z')

axis equal
view([0,0,180])
% end of plot surfaces and fill
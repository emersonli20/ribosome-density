% brushedData15 = csvread("5991_L2_ts001_1.5.csv")

x = brushedData15(:,1)
y = brushedData15(:,2)
z = brushedData15(:,3)

f = fit([x,z], y, 'poly22')
plot(f,[x,z], y)
xlabel('x')
ylabel('y')
zlabel('z')

axis equal

% f2 = fit(x,y, 'poly2')
% plot(f2, x,y)

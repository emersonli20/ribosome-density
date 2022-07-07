clc
densities = csvread("shells_ribosome_densities.csv");
x = shells(:,1,11:10:150);
x = x(:);
y = shells(:,2,11:10:150);
y = y(:);
z = shells(:,3,11:10:150);
z = z(:);
d = zeros(7392*14,1);


for i=1:14;
     low = 7392*(i-1)+1;
     high = 7392*i;
     j = i*10+1
     d(low:high)=densities(j);
     densities(i)
end 

scatter3(x,y,z,10,d,'filled')
xlabel('x')
ylabel('y')
zlabel('z')
ax = gca
axis equal
view([0,0,180])

cb = colorbar;
cb.Label.String = 'Average ribosome density';
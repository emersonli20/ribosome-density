function make_isosurfaces(shells_coords,densities,stepsize)

    shells = shells_coords;
    n = size(shells, 1)
    % densities = csvread("shells_ribosome_densities.csv");
    s = ceil(150/stepsize);
    
    x = shells(:,1,1:stepsize:150);
    x = x(:);
    y = shells(:,2,1:stepsize:150);
    y = y(:);
    z = shells(:,3,1:stepsize:150);
    z = z(:);
    d = zeros(n*s,1);
    
    
    for i=0:(s-1);
         low = n*i+1;
         high = n*(i+1);
         j = i*stepsize+1;
         d(low:high)=densities(j);
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
end

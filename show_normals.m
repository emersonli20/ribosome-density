function show_normals(ptcloud,stepsize,normals)
    u= normals(1:end, 1);
    v= normals(1:end, 2);
    w= normals(1:end, 3);
    x= ptcloud.Location(1:stepsize:end, 1);
    y= ptcloud.Location(1:stepsize:end, 2);
    z= ptcloud.Location(1:stepsize:end, 3);

    sensorCenter = [-300,0,0]; 
    for k = 1 : numel(x)
       p1 = sensorCenter - [x(k),y(k),z(k)];
       p2 = [u(k),v(k),w(k)];
       % Flip the normal vector if it is not pointing towards the sensor.
       angle = atan2(norm(cross(p1,p2)),p1*p2');
       if angle > pi/2 || angle < -pi/2
           u(k) = -u(k);
           v(k) = -v(k);
           w(k) = -w(k);
       end
    end

    figure
    pcshow(ptcloud)
    title('Adjusted Normals of Point Cloud')
    hold on
    quiver3(x, y, z, u, v, w);
    xlabel('x');
    ylabel('y');
    zlabel('z');
    hold off
end

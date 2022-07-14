function adjusted_normals = get_adjusted_normals(ptcloud, normals, sensorCenter)
    
    x= ptcloud.Location(1:end, 1);
    y= ptcloud.Location(1:end, 2);
    z= ptcloud.Location(1:end, 3);

    u= normals(1:end, 1);
    v= normals(1:end, 2);
    w= normals(1:end, 3);

    n = numel(x);

    % CHANGE the sensorCenter coords using the pointcloud visualization
    for k = 1 : n
       p1 = sensorCenter - [x(k),y(k),z(k)];
       p2 = [u(k),v(k),w(k)];
    %  Flip the normal vector if it is not pointing towards the sensor.
       angle = atan2(norm(cross(p1,p2)),p1*p2');
       if angle > pi/2 || angle < -pi/2
           u(k) = -u(k);
           v(k) = -v(k);
           w(k) = -w(k);
       end
    end
    adjusted_normals = cat(2,u,v,w);
end

function show_normals(ptcloud,normals)
    u= normals(1:end, 1);
    v= normals(1:end, 2);
    w= normals(1:end, 3);
    x= ptcloud.Location(1:end, 1);
    y= ptcloud.Location(1:end, 2);
    z= ptcloud.Location(1:end, 3);
    figure
    pcshow(ptcloud)
    title('Adjusted Normals of Point Cloud')
    hold on
    quiver3(x, y, z, u, v, w);
    xlabel('x');
    ylabel('y');
    zlabel('z');
    axis equal
    view([0,0,180])
    hold off
end
function shells = membrane_boundary_shells(coords, adjusted_normals, stepsize)
    n = numel(adjusted_normals)/3;
    shells = zeros(n, 3, 2);
    for i = 1: n
        shells(i,1,1) = coords(i,1) - adjusted_normals(i,1)*stepsize;
        shells(i,2,1) = coords(i,2) - adjusted_normals(i,2)*stepsize;
        shells(i,3,1) = coords(i,3) - adjusted_normals(i,3)*stepsize;
    end
    for i = 1: n
        shells(i,1,2) = coords(i,1) + adjusted_normals(i,1)*stepsize;
        shells(i,2,2) = coords(i,2) + adjusted_normals(i,2)*stepsize;
        shells(i,3,2) = coords(i,3) + adjusted_normals(i,3)*stepsize;
    end
    
end
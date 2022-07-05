function shells = make_shells(coords, normals, s)
    n = numel(normals)/3;
    shells = zeros(n, 3, s);
    for j = 1:s
        for i = 1: n
            shells(i,1,j) = coords(i,1) - normals(i,1)*j;
            shells(i,2,j) = coords(i,2) - normals(i,2)*j;
            shells(i,3,j) = coords(i,3) - normals(i,3)*j;
        end
    end
end
function shells = make_shells(coords, adjusted_normals, shell_number)
    n = numel(adjusted_normals)/3;
    shells = zeros(n, 3, shell_number);
    for j = 0:(shell_number-1)
        for i = 1: n
            shells(i,1,j+1) = coords(i,1) + adjusted_normals(i,1)*j;
            shells(i,2,j+1) = coords(i,2) + adjusted_normals(i,2)*j;
            shells(i,3,j+1) = coords(i,3) + adjusted_normals(i,3)*j;
        end
    end
end

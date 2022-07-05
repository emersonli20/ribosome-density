function y_flipped_normals = manually_flip_y(normals)
    for i = 1: (numel(normals)/3)
        y_flipped_normals = normals;
        if normals(i,2)>0
            y_flipped_normals(i,1) = -normals(i,1);
            y_flipped_normals(i,2) = -normals(i,2);
            y_flipped_normals(i,3) = -normals(i,3);
        end
    end
end


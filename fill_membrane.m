coeffs_1 = coeffvalues(surface1)
coeffs_2 = coeffvalues(surface2)

p00_1 = coeffs_1(1)
p10_1 = coeffs_1(2)
p01_1 = coeffs_1(3)
p20_1 = coeffs_1(4)
p11_1 = coeffs_1(5)
p30_1 = coeffs_1(6)
p21_1 = coeffs_1(7)
p40_1 = coeffs_1(8)
p31_1 = coeffs_1(9)

p00_2 = coeffs_2(1)
p10_2 = coeffs_2(2)
p01_2 = coeffs_2(3)
p20_2 = coeffs_2(4)
p11_2 = coeffs_2(5)
p30_2 = coeffs_2(6)
p21_2 = coeffs_2(7)
p40_2 = coeffs_2(8)
p31_2 = coeffs_2(9)


csvwrite("coeffs_1.csv", coeffs_1)
csvwrite("coeffs_2.csv", coeffs_2)

% fill = double.empty(0,3)
% 
% for i = x_min : 5 : x_max
%     for j = y_min : 5 : y_max
%         for k = z_min  : 5 : z_max
%             k1 = p00_1 + p10_1 * i + p01_1 * j + p20_1 * i^2 + p11_1 * i * j
%             k2 = p00_2 + p10_2 * i + p01_2 * j + p20_2 * i^2 + p11_2 * i * j
%             bigK = max([k1,k2])
%             smallK = min([k1,k2])
% 
%             if k > smallK && k < bigK
%                 fill = vertcat(fill, [i,j,k])
%             end
%         end
%     end
% end
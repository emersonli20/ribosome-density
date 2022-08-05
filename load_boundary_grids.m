% load membrane boundary grid
membrane_boundaries = csvread("5991_L2_ts004_membrane_boundaries_6.csv")
x1 = membrane_boundaries(:,1)
y1 = membrane_boundaries(:,2)
z1 = membrane_boundaries(:,3)
x2 = membrane_boundaries(:,4)
y2 = membrane_boundaries(:,5)
z2 = membrane_boundaries(:,6)
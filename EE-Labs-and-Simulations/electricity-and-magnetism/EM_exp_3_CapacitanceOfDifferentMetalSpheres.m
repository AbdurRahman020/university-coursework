clear; clc; close all;

% applied voltage (kV)
U2 = 0:0.5:5;
% mesured voltages (V) for r1 = 1cm, r2 = 2cm and r3 = 6cm  
U1_r1 = [0, 1.6, 3.6, 5.6, 7.7, 9.7, 11.7, 12.8, 14.7, 16.7, 18.8];
U1_r2 = [0, 2.8, 5.1, 8, 9.8, 11.7, 15.3, 17.0, 19.5, 21.5, 23.8]; 
U1_r3 = [0, 3.6, 7.1, 10.3, 14.2, 17.6, 21.1, 24.4, 27.2, 31.7, 34.7];

p1 = polyfit(U2, U1_r1, 1);
p2 = polyfit(U2, U1_r2, 1);
p3 = polyfit(U2, U1_r3, 1);

U1_r1_fit = polyval(p1, U2);
U1_r2_fit = polyval(p2, U2);
U1_r3_fit = polyval(p3, U2);

figure;
plot(U2, U1_r1, 'o', 'DisplayName', 'R_1', 'LineWidth', 2);
hold on;
plot(U2, U1_r2, 'x', 'DisplayName', 'R_2', 'LineWidth', 2);
plot(U2, U1_r3, 's', 'DisplayName', 'R_3', 'LineWidth', 2);

plot(U2, U1_r1_fit, '-r', 'DisplayName', 'R_1 line fit', 'LineWidth', 1.25);
plot(U2, U1_r2_fit, '-g', 'DisplayName', 'R_2 line fit', 'LineWidth', 1.25);
plot(U2, U1_r3_fit, '-b', 'DisplayName', 'R_3 line fit', 'LineWidth', 1.25);

xlabel('U_2 (kV)'); ylabel('U_1 (mV)');
title('Plot of U_1 vs U_2 for spheres of radii R_1, R_2 & R_3');
legend show;

grid on; grid minor;
hold off;
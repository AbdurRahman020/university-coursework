clear; clc; close all;

% current (A)
I = 0.2:0.2:1.4;
% deflection of Galvanometer
theta = [80, 100, 120, 140, 150, 150, 150];

p = polyfit(I, theta, 2);
theta_fit = polyval(p, I);

figure;
plot(I, theta, '-o', 'DisplayName', 'Data', 'LineWidth', 2);
hold on;
plot(I, theta_fit, 'r-', 'DisplayName', 'Quadratic fit', 'LineWidth', 1.25);

xlabel('I (A)'); ylabel('\theta ');
title('Initial Curve of Ferromagnetic material');
legend show;

grid on; grid minor;
hold off;

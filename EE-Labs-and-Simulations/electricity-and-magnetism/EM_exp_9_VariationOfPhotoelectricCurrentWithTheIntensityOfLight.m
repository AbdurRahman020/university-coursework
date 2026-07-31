clear; clc; close all;

% distance of lamp from photo cell (m)
d = 0.85:-0.05:0.45;
% intensity of light (per meter square)
In = 1./d.^2;
% photoelectric current (uA)
I = [26, 29, 34, 40, 46, 56, 68, 84, 105];

p_In = polyfit(In, I, 1);
In_fit = polyval(p_In, In);

figure;
plot(In, I, 'x', 'DisplayName', 'Data Points', 'LineWidth', 2);
hold on;
plot(In, In_fit, 'r-', 'DisplayName', 'Linear Fit', 'LineWidth', 1.25);

xlabel('Intensity of Light'); ylabel('Photoelectric Current');
title('Variation of Photoelectric Current with the Intensity of Light');
legend show;

grid on; grid minor;
hold off;

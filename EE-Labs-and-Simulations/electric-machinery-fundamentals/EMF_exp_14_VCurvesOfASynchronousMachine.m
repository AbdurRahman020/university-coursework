clear; clc; close all;

% excitation current (A)
I_DC = [3.715, 3.287, 2.733, 2.318, 1.773, 1.326, 1.01, 0.591, 0.376, 0.320];
% stator current (A)
I_L = [1.22, 0.98, 0.66, 0.45, 0.24, 0.44, 0.63, 0.92, 1.10, 1.22];

% Gaussian V-curve model 
% I_L = a + b * exp(-(I_DC - c)^2 / (2*sigma^2))
f = @(p,x) p(1) + p(2)*exp(-((x - p(3)).^2) ./ (2*p(4)^2));

% initial parameter guess: [a  b  c  sigma]
p0 = [0.2, 1, 2, 0.7];

% curve fitting
p_fit = lsqcurvefit(f, p0, I_DC, I_L);

% smooth fitted curve for plotting
I_DC_smooth = linspace(min(I_DC), max(I_DC), 200);
I_L_fit = f(p_fit, I_DC_smooth);

% plotting the data
figure;
plot(I_DC, I_L, 'x', 'LineWidth', 2, 'MarkerSize', 7); hold on;
plot(I_DC_smooth, I_L_fit, '--', 'LineWidth', 2);

xlabel('Excitation Current: I_{DC} (A)'); ylabel('Line Current: I_{L} (A)');
title('V-curve of the Synchronous Machine');
legend('Experimental Data', 'Gaussian Fit', 'Location', 'north');
grid on; grid minor;
hold off;

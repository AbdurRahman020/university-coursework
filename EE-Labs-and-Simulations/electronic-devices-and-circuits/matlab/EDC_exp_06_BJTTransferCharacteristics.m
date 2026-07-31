clear; clc; close all;

% given data
I_C  = [3e-9, 3e-9, 1.4e-6, 1.4e-5, 1.14e-5, 6.92e-5, 1.695e-4, 0.82e-3, ...
    2.36e-3, 6.56e-3, 28.4e-3]; % mA
V_BE = [0.11, 0.19, 0.32, 0.36, 0.41, 0.48, 0.51, 0.57, 0.61, 0.66, 0.7]; % V

% graph: I_C vs V_BE
exp_fit = fit(V_BE.', I_C.', 'exp1');

% applying curve fitting
V_BE_fit = linspace(min(V_BE), max(V_BE), 200);
I_C_fit = exp_fit(V_BE_fit);

% plotting graph
figure;
plot(V_BE, I_C, 'x', 'LineWidth', 2, 'MarkerSize', 7); hold on;
plot(V_BE_fit, I_C_fit, '--', 'LineWidth', 2);

xlabel('V_{BE} (V)'); ylabel('I_C (A)');
title('I_C vs V_{BE}');
legend('Experimental Data', 'Exponential Fit', 'Location', 'northwest');
grid on; grid minor;
hold off;

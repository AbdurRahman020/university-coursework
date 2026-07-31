clear; clc; close all;

% given data
I_C  = [0.14, 0.56, 1.3, 5.1, 10.3, 15.1]; % mA
I_B  = [0.48, 2.55, 4.57, 15.15, 39.46, 49.6]; % µA

% graph: I_C vs I_B
p_linear = polyfit(I_B, I_C, 1); 
I_C_fit = polyval(p_linear, I_B);

figure;
plot(I_B, I_C, 'x', 'LineWidth', 2, 'MarkerSize', 7); hold on;
plot(I_B, I_C_fit, '--', 'LineWidth', 2);

xlabel('I_B (\muA)'); ylabel('I_C (mA)');
title('I_C vs I_B');
legend('Experimental Data', 'Linear Fit', 'Location', 'northwest');
grid on; grid minor;
hold off;

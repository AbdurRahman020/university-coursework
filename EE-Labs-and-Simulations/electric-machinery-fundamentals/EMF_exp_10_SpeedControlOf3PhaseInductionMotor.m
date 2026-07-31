clear; clc; close all;

%% Speed Control by VFD

% frequency varied by VFD (Hz)
f = 4:4:40;
% corresponding speed change (rpm)
n_f = [251.06, 488.1, 727.03, 966.88, 1207.6, 1443.2, 1694.5, 1931.1, ...
    2163.5, 2409.2];

% fit a linear model between frequency and angular speed
p_linear = polyfit(f, n_f, 1); 
% get the fitted angular speed
n_f_fit = polyval(p_linear, f);

% plotting the data between 'f' and 'n_f'
figure;
plot(f, n_f, 'x', 'LineWidth', 2, 'MarkerSize', 7); hold on;
plot(f, n_f_fit, '--', 'LineWidth', 2);

xlabel('Frequecny: f (Hz)'); ylabel('Speed: N (rpm)');
title('Speed vs Frequncy');
legend('Experimental Data', 'Fitted Line', 'Location', 'northwest');
grid on; grid minor;
hold off;

%% Speed Control by Line Voltage variation

% varying supply voltage (Volts)
V_line = [32, 36, 44, 48, 53, 58, 64, 70, 73, 77];
% corresponding speed change (rpm)
n_v = [151, 274, 630, 1073, 1709, 2054, 2316, 2452, 2508, 2573];

% fit a model between line voltage and angular speed
p_fitted = polyfit(V_line, n_v, 5);
% get the fitted angular speed
n_v_fit = polyval(p_fitted, V_line);

% plotting the data between 'V_line' and 'n_f'
figure;
plot(V_line, n_v, 'x', 'LineWidth', 2, 'MarkerSize', 7); hold on;
plot(V_line, n_v_fit, '--', 'LineWidth', 2);

xlabel('Line Voltage: V_{L} (V)'); ylabel('Speed: N (rpm)');
title('Speed vs Line Voltage');
legend('Experimental Data', 'Fitted Line', 'Location', 'northwest');
grid on; grid minor;
hold off;

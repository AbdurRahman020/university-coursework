clear; clc; close all;

%% Frequency Control / Throttle Control / Governer Control

% speed of prime mover (rpm)
n_s = [1510, 1696, 1863, 2219, 2424, 2569, 2646, 2778, 2882, 3000];
% frequency varied by VFD (Hz)
f = [25.13, 28.41, 31.06, 37.1, 40.32, 42.92, 44.25, 46.08, 48.03, 50.25];


% fit a linear model between frequency and angular speed
p_linear = polyfit(n_s, f, 1); 
% get the fitted angular speed
f_fit = polyval(p_linear, n_s);

% plotting the data between 'f' and 'n_f'
figure;
plot(n_s, f, 'x', 'LineWidth', 2, 'MarkerSize', 7); hold on;
plot(n_s, f_fit, '--', 'LineWidth', 2);

xlabel('Speed: N_{s} (rpm)'); ylabel('Frequency: f (Hz)');
title('Frequency Control of Synchronous Generator');
legend('Experimental Data', 'Fitted Line', 'Location', 'northwest');
grid on; grid minor;
hold off;

%% Voltage Control / Excitaion Control

% excitation voltage (V)
V_DC = [7.88, 8.90, 9.77, 11.28, 12.55, 14.42, 15.88, 17.88, 20.54, 22.88];
% line voltage (Volts)
V_line = [160.5, 173.51, 184.65, 196.90, 204.39, 215.93, 220.34, ...
    228.14, 235.75, 237.55];

% fit a model between excitation voltage and line voltage
p_fitted = polyfit(V_line, V_DC, 2);
% get the fitted line voltage
n_v_fit = polyval(p_fitted, V_line);

% plotting the data between 'V_DC' and 'V_line'
figure;
plot(V_line, V_DC, 'x', 'LineWidth', 2, 'MarkerSize', 7); hold on;
plot(V_line, n_v_fit, '--', 'LineWidth', 2);

xlabel('Excitation Voltage: V_{DC} (V)'); ylabel('Line Voltage: V_L (V)');
title('Voltage Control of Synchronous Generator');
legend('Experimental Data', 'Fitted Line', 'Location', 'northwest');
grid on; grid minor;
hold off;

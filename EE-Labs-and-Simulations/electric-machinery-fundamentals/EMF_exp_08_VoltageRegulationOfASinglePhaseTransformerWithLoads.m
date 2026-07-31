clear; clc; close all;

% no-load voltage (V)
V_nl = 135;

%% Resistive Load

% load currents (A) for resistive loads
Il_R = [0.319, 0.512, 0.852, 1.011, 1.194, 1.367, 1.654, 1.829, ...
    2.126, 2.292];
% corresponding secondary voltages (V) 
Vs_R = [134.6, 134.3, 133.8, 133.5, 133.3, 132.9, 132.4, 132.1, ...
    131.5, 131.2];

% percentage voltage regulation for resistive loads
V_R_regulation = (V_nl - Vs_R)/V_nl * 100;

% fit a model between 'load current' and '% voltage regulation'
p_fitted = polyfit(Il_R, V_R_regulation, 3);
% get the fitted value of '% voltage regulation'
V_R_regulation_fitted = polyval(p_fitted, Il_R);

% plotting the data between 'Load Current' and '% Regulation'
figure;
plot(Il_R, V_R_regulation, 'x', 'LineWidth', 2, 'MarkerSize', 7); hold on;
plot(Il_R, V_R_regulation_fitted, '--', 'LineWidth', 2);

xlabel('Load Current (A)'); ylabel('% Voltage Regulation');
title('Voltage Regulation of the Resistive Load');
legend('Experimental Data', 'Fitted Line', 'Location', 'northwest');
grid on; grid minor;
hold off;

%% Inductive Load

% load currents (A) for inductive loads
Il_L = [0.489, 0.984, 1.275, 1.556, 1.849, 2.126, 2.343, 2.565, ...
    2.835, 3.066];
% corresponding secondary voltages (V) 
Vs_L = [135.6, 135.4, 135.3, 135.2, 135, 134.9, 134.7, 134.6, 134.3, 134.2];

% percentage voltage regulation for inductive loads
V_L_regulation = (V_nl - Vs_L)/V_nl * 100;

% fit a model between 'load current' and '% voltage regulation'
p_fitted = polyfit(Il_L, V_L_regulation, 3);
% get the fitted value of '% voltage regulation'
V_L_regulation_fitted = polyval(p_fitted, Il_L);

% plotting the data between 'Load Current' and '% Regulation'
figure;
plot(Il_L, V_L_regulation, 'x', 'LineWidth', 2, 'MarkerSize', 7); hold on;
plot(Il_L, V_L_regulation_fitted, '--', 'LineWidth', 2);

xlabel('Load Current (A)'); ylabel('% Voltage Regulation');
title('Voltage Regulation of the Inductive Load');
legend('Experimental Data', 'Fitted Line', 'Location', 'northwest');
grid on; grid minor;
hold off;

%% Capacitive Load

% load currents (A) for capacitive loads
Il_C = [0.367, 0.737, 1.151, 1.512, 1.917];
% corresponding secondary voltages (V) 
Vs_C = [137.3, 137.6, 137.9, 138.1, 138.5];

% percentage voltage regulation for capacitive loads
V_C_regulation = (V_nl - Vs_C)/V_nl * 100;

% fit a model between 'load current' and '% voltage regulation'
p_fitted = polyfit(Il_C, V_C_regulation, 2);
% get the fitted value of '% voltage regulation'
V_C_regulation_fitted = polyval(p_fitted, Il_C);

% plotting the data between 'Load Current' and '% Regulation'
figure;
plot(Il_C, V_C_regulation, 'x', 'LineWidth', 2, 'MarkerSize', 7); hold on;
plot(Il_C, V_C_regulation_fitted, '--', 'LineWidth', 2);

xlabel('Load Current (A)'); ylabel('% Voltage Regulation');
title('Voltage Regulation of the Capacitive Load');
legend('Experimental Data', 'Fitted Line', 'Location', 'northeast');
grid on; grid minor;
hold off;

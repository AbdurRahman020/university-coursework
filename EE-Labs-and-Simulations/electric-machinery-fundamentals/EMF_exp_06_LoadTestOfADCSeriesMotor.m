clear; clc; close all;

% motor input voltage (V)
V_in = [110, 109, 108, 107, 107, 106, 106, 105];
% motor input current (A)
I_in = [1.92, 2.43, 2.65, 2.82, 2.96, 3.06, 3.16, 3.24];

% speed (rpm)
N = [2273, 1896, 1757, 1653, 1586, 1535, 1480, 1433];

% load voltage (V)
V_l = [209, 161, 142, 130, 116, 104, 92, 82];
% load current (A)
I_l = [0, 0.36, 0.55, 0.71, 0.87, 1, 1.18, 1.36];

% calculate input and output power (W)
P_in = V_in .* I_in;  P_out = V_l .* I_l;

% efficiency calculation
eff = P_out ./ P_in * 100;

% fit the data for P_l vs efficiency
fit_params_eff = polyfit(P_out, eff, 2);
% fit the data for P_l vs N 
fit_params = polyfit(P_out, N, 2);

% calculate the fitted values of N
N_fitted = polyval(fit_params, P_out); 
% calculate the fitted efficiency values
eff_fitted = polyval(fit_params_eff, P_out);

% plotting the data between 'P_out' and 'N'
figure; 
hold on;
plot(P_out, N, 'x', 'DisplayName', 'Experimental Data', ...
    'LineWidth', 1.5, 'MarkerSize', 6);
plot(P_out, N_fitted, '--', 'DisplayName', 'Fitted Line', ...
    'LineWidth', 1.5);
xlabel('{P_{out}} (W)'); ylabel('{N} (rpm)');
title('{P_{out}} vs {N}');
legend show;
grid on;  grid minor;
hold off;

% plotting the data between 'P_out' and 'eff'
figure; 
hold on;
plot(P_out, eff, 'x', 'DisplayName', 'Experimental Data', ...
    'LineWidth', 1.5, 'MarkerSize', 6);
plot(P_out, eff_fitted, '--', 'DisplayName', 'Fitted Line', ...
    'LineWidth', 1.5);
xlabel('{P_{out}} (W)'); ylabel('{Efficiency} (%)');
title('{P_{out}} vs {Efficiency}');
legend show;
grid on;  grid minor;
hold off;
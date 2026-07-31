clear; clc; close all;

%% Graph between Load Voltage and Load Current

% load voltage (V)
V_L = [134.2, 131.8, 128.9, 125.6, 121.9, 117.3, 113.3, 108.3, 100.6, 93.7];
% load current (A)
I_L = [1.407, 1.513, 1.65, 1.78, 1.927, 2.103, 2.252, 2.419, 2.668, 2.861];

% fit a model between load current and load voltage
fit_param1 = polyfit(I_L, V_L, 2);

% get the fitted vlaues of load voltage
fitted_V_L = polyval(fit_param1, I_L);

% plot the data
figure;
hold on;
plot(I_L, V_L, 'x', 'DisplayName', 'Experimental Data', ...
    'LineWidth', 2, 'MarkerSize', 7);
plot(I_L, fitted_V_L, '--', 'DisplayName', 'Fitted Line', 'LineWidth', 2);

xlabel('I_L (A)'); ylabel('V_L (V)');  
title('V_L vs I_L');
legend show;

grid on; grid minor;
hold off;

%% Graph between Induced EMF and Armature Current

% armature current (A)
I_A = [1.54, 1.644, 1.778, 1.905, 2.048, 2.219, 2.365, 2.526, 2.768, 2.954];
% induced emf (V)
E_A = V_L + I_A*8; 

% fit a model between armature current and induced emf
fit_param1 = polyfit(I_A, E_A, 2);

% get the fitted induced emf values
fitted_E_A = polyval(fit_param1, I_A);

% plot the data
figure;
hold on;
plot(I_A, E_A, 'x', 'DisplayName', 'Experimental Data', ...
    'LineWidth', 2, 'MarkerSize', 7);
plot(I_A, fitted_E_A, '--', 'DisplayName', 'Fitted Line', 'LineWidth', 2);

xlabel('Armature Current:I_A (A)'); ylabel('Induced Voltage:E (V)');  
title('E_A vs I_A');
legend show;

grid on; grid minor;
hold off;

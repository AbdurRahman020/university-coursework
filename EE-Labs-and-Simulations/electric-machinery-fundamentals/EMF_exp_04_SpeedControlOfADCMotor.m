clear; clc; close all;

%% By Varying Armature Voltage

% armature voltage (V)
V_a = [60, 70.2, 80.4, 90.6, 100.8, 110.6, 120.8, 130.4, 140.1, 150.4];
% speed (RPM) due to change in V_a, field current is kept constant
N_V_a = [630.21, 742.56, 854.52, 967.24, 1079.3, 1189.2, 1300.4, ...
    1407.1, 1515.4, 1627.2];

% converting RPM to rad/s
omega_V_a = 2*pi*N_V_a/60;
% fit a linear model between armature voltage and angular frequency
fit_param1 = polyfit(V_a, omega_V_a, 1);

% get the fitted angular frequencies
omega_fitted1 = polyval(fit_param1, V_a);

% plot the data
figure;
hold on;
plot(V_a, omega_V_a, 'x', 'DisplayName', 'Experimental Data', ...
    'LineWidth', 1, 'MarkerSize', 6);
plot(V_a, omega_fitted1, '--', 'DisplayName', 'Fitted Line', 'LineWidth', 1);

xlabel('{V_a} (V)'); ylabel('{\omega} (rad/s)');  
title('{V_a} vs {\omega} for DC motor (sperately excited)');
legend show;

grid on; grid minor;
hold off;

%% By Varying Field Current

% field current (mA) 
I_f = [184.2, 175.6, 165.4, 153.0, 142.6, 133.5, 122.4, 112.2, 100.5, ...
    92.0, 81.2, 72.1, 64.4, 54.6];
% speed (RPM) due to change in I_f
N_I_f = [1310, 1316.5, 1332.2, 1349.2, 1366.6, 1383.9, 1408.6, 1438.7, ...
    1489.3, 1519.1, 1592.7, 1659.3, 1732.3, 1854.9];

% converting RPM to rad/s
omega_I_f = 2*pi*N_I_f/60;

% fit a cubic model between field current and angular frequency
fit_param2 = polyfit(I_f, omega_I_f, 3);
% get the fitted angular frequencies
omega_fitted2 = polyval(fit_param2, I_f);

figure;
hold on;
plot(I_f, omega_I_f, 'x', 'DisplayName', 'Experimental Data', ...
    'LineWidth', 1, 'MarkerSize', 6);
plot(I_f, omega_fitted2, '--', 'DisplayName', 'Fitted Line', 'LineWidth', 1);

xlabel('{I_f} (mA)'); ylabel('{\omega} (rad/s)');  
title('{I_f} vs {\omega} for DC motor (sperately excited)');
legend show;

grid on; grid minor;
hold off;

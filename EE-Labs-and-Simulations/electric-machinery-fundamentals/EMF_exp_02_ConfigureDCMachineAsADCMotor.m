clear; clc; close all;

%% Seperately Excited DC Motor

% armature voltage (V)
V_a1 = [100, 110.2, 120.6, 129.5, 140.3]; 
% angular frequency (RPM)
N1 = [1059, 1170, 1282, 1383, 1504];

% field current (mA)
I_f = [87, 100, 112, 124, 138];
% angular frequency (RPM)
N2 = [1286, 1224, 1195, 1164, 1142];

% converting RPM to rad/s
omega1 = 2*pi*N1/60; omega2 = 2*pi*N2/60;

% fit a linear model between armature voltage and angular frequency
fit_params1 = polyfit(V_a1, omega1, 1);
% fit a quadratic model between field current and angular frequency
fit_params2 = polyfit(I_f, omega2, 2);

% get the fitted angular frequencies
omega_fitted1 = polyval(fit_params1, V_a1);
omega_fitted2 = polyval(fit_params2, I_f);

% plot the data
figure;
hold on;
plot(V_a1, omega1, 'x', 'DisplayName', 'Experimental Data', ...
    'LineWidth', 2, 'MarkerSize', 7);
plot(V_a1, omega_fitted1, '--', 'DisplayName', 'Fitted Line', 'LineWidth', 2);

xlabel('{V_a} (V)'); ylabel('{\omega} (rad/s)');  
title('{V_a} vs {\omega} for DC motor (sperately excited)');
legend show;

grid on; grid minor;
hold off;

figure;
hold on;
plot(I_f, omega2, 'x', 'DisplayName', 'Experimental Data', ...
    'LineWidth', 2, 'MarkerSize', 7);
plot(I_f, omega_fitted2, '--', 'DisplayName', 'Fitted Line', 'LineWidth', 2);

xlabel('{I_f} (mA)'); ylabel('{\omega} (rad/s)');  
title('{I_f} vs {\omega} for DC motor (sperately excited)');
legend show;

grid on; grid minor;
hold off;

%% Shunt DC Motor

% armature voltage (V)
V_a2 = [100.4, 110.5, 120.5, 130.7, 140.5];
% angular frequency (RPM)
N3 = [1368, 1441, 1506, 1594, 1669];

% converting RPM to rad/s
omega3 = 2*pi*N3/60;

% fit a linear model between field current and angular frequency
fit_params3 = polyfit(V_a2, omega3, 1);

% get the fitted angular frequencies
omega_fitted3 = polyval(fit_params3, V_a2);

% plot the data
figure;
hold on;
plot(V_a2, omega3, 'x', 'DisplayName', 'Experimental Data', ...
    'LineWidth', 1, 'MarkerSize', 6);
plot(V_a2, omega_fitted3, '--', 'DisplayName', 'Fitted Line', 'LineWidth', 1);

xlabel('{V_a} (V)'); ylabel('{\omega} (rad/s)');  
title('{V_a} vs {\omega} for DC motor (shunt)');
legend show;

grid on; grid minor;
hold off;

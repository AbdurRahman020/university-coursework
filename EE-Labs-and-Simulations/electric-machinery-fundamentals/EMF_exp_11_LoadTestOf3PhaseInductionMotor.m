clear; clc; close all;

P_in = [60, 118, 158, 194, 231, 336];
M_net = [0.5, 1, 1.25, 1.5, 1.75, 2.5];

g = 9.8;
F_net = g*M_net;

r = 7.3e-2;
tau = r*F_net; 

n = [1388, 1359, 1339, 1300, 1280, 1250];
omega = 2*pi*n/60;

P_out = tau.*omega;
eff = (P_out./P_in) * 100;

fit_param = polyfit(omega, tau, 2);
tau_fitted = polyval(fit_param, omega);

figure;
hold on;
plot(omega, tau, 'x', 'DisplayName', 'Experimental Data', ...
    'LineWidth', 2, 'MarkerSize', 6);
plot(omega, tau_fitted, '--', 'DisplayName', 'Fitted Line', 'LineWidth', 2);

xlabel('{\omega} (rad/s)'); ylabel('{\tau} (Nm)');  
title('{\tau} VS {\omega} for 3 {\phi} induction motor');
legend show;

grid on; grid minor;
hold off;

clear; clc; close all;

% temperature range (K)
T = 328:5:373;
% probe voltage (V)
U_p = [8.43, 7.29, 5.77, 5.07, 4.13, 3.51, 2.91, 2.45, 2.12, 1.91];
% given constants for Ge specimen: lenght (l), area of cross-section (A)
% and current through it (I)
l = 20e-3; A = 10e-6; I = 5e-3;

% conductivity (1/(ohm*mm))
sigma = l * I ./ (A * U_p); ln_sg = log(sigma);
% reciporcal of absolute temprature (1/K)
r_T = 1 ./T;

p_Up = polyfit(T, U_p, 3);
p_rT = polyfit(r_T, ln_sg, 1);

U_p_fit = polyval(p_Up, T);
ln_sg_fit = polyval(p_rT, r_T);

figure;

subplot(1,2,1);
plot(T, U_p, 'x', 'DisplayName', 'U_p points', 'LineWidth', 2)
hold on;
plot(T, U_p_fit, 'DisplayName', 'U_p', 'LineWidth', 1.25)

xlabel('Temperature {T} (K)'); ylabel('Probe Voltage {U_P} (V)');  
title('Probe Voltage as function of the temprature');
legend show;

grid on; grid minor;

subplot(1,2,2);
plot(r_T, ln_sg, 'x', 'DisplayName', 'ln(\sigma) points', 'LineWidth', 2)
hold on;
plot(r_T, ln_sg_fit, 'DisplayName', 'ln(\sigma)', 'LineWidth', 1.25)

xlabel('Temperature (K)');  ylabel('ln(\sigma) (\Omega^{-1} mm^{-1})');  
title('Conductivity versus the reciprocal of absolute temprature');
legend show;

grid on; grid minor;
hold off;

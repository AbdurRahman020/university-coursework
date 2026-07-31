clear; clc; close all;

% armature current
I_a = [0.755, 0.805, 0.865, 0.975, 1.055, 1.185];

% no load voltage
V_ta = [74.4, 74.4, 74.4, 74.4, 74.4, 74.4];

% terminal voltages
V_tb = [66.3, 65.5, 64.6, 64.2, 64, 63.8];
V_tc = [54.9, 54, 52.5, 50.6, 48.3, 46.3];

% fitting data I_a vs V_tb
p_tb = polyfit(I_a, V_tb, 1);
% fitting data I_a vs V_tc
p_tc = polyfit(I_a, V_tc, 1);

% calculate the fitted values of V_tb
V_tb_fit = polyval(p_tb, I_a);
% calculate the fitted values of V_tc
V_tc_fit = polyval(p_tc, I_a);

figure;
plot(I_a, V_ta, '-.', 'DisplayName', 'V_{ta}', 'LineWidth', 1.5);
hold on;
plot(I_a, V_tb, 'x', 'DisplayName', 'V_{tb}', 'LineWidth', 1.5);
plot(I_a, V_tc, 'x', 'DisplayName', 'V_{tc}', 'LineWidth', 1.5);
plot(I_a, V_tb_fit, '--', 'DisplayName', 'Fitted V_{tb}', 'LineWidth', 1.5);
plot(I_a, V_tc_fit, '--', 'DisplayName', 'Fitted V_{tc}', 'LineWidth', 1.5);

xlabel('I_a (Amperes)'); ylabel('Voltage (Volts)');
title('Graph between I_a and V_{ta}, V_{tb}, V_{tc}');
legend show;
grid on;  grid minor;
hold off;

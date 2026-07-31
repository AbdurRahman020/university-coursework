clear; clc; close all;

T = 25:5:70;

CuNi = [172, 173, 173, 171.6, 171.7, 171.6, 171.3, 172, 174, 175];
C = [1002, 1003, 1001, 1011, 1000, 1011, 1009, 1000, 1000, 1000];
Met = [997, 1000, 991, 983, 960, 963, 964, 956, 959, 954];
NTC = [966, 781, 669, 525, 447, 378, 317, 280, 243, 214];
PTC = [56.4, 61.7, 67.9, 79.7, 95, 121.4, 165, 258, 462, 890];

p_CuNi = polyfit(T, CuNi, 1);
p_C = polyfit(T, C, 1);
p_Met = polyfit(T, Met, 1);
p_NTC = polyfit(T, NTC, 5);
p_PTC = polyfit(T, PTC, 6);

CuNi_fit = polyval(p_CuNi, T);
C_fit = polyval(p_C, T);
Met_fit = polyval(p_Met, T);
NTC_fit = polyval(p_NTC, T);
PTC_fit = polyval(p_PTC, T);

figure;
plot(T, CuNi, 'x', 'DisplayName', 'CuNi points', 'LineWidth', 2, 'Color', 'b');
hold on;
plot(T, C, 'x', 'DisplayName', 'C points', 'LineWidth', 2, 'Color', 'b');
plot(T, Met, 'x', 'DisplayName', 'Met points', 'LineWidth', 2, 'Color', 'b');
plot(T, NTC, 'x', 'DisplayName', 'NTC points', 'LineWidth', 2, 'Color', 'b');
plot(T, PTC, 'x', 'DisplayName', 'PTC points', 'LineWidth', 2, 'Color', 'b');

plot(T, CuNi_fit, '-', 'DisplayName', 'CuNi', 'LineWidth', 1.25);
plot(T, C_fit, '-', 'DisplayName', 'C', 'LineWidth', 1.25)
plot(T, Met_fit, '-', 'DisplayName', 'Met','LineWidth', 1.25)
plot(T, NTC_fit, '-', 'DisplayName', 'NTC', 'LineWidth', 1.25)
plot(T, PTC_fit, '-', 'DisplayName', 'PTC', 'LineWidth', 1.25)

xlabel('T (^{o}C)'); ylabel('R (\Omega)');
title('Resistance of some Materials & Components as a function of Temprature');
legend show;

grid on; grid minor;
hold off;

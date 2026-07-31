clear; clc; close all;

% applied voltage (kV)
U = 0:0.1:1;
% stored charge on plates, without dieletric in-between plates (nC)
Q1 = 220*[0, 0.021, 0.051, 0.079, 0.120, 0.134, 0.176, 0.231, 0.240, 0.264, 0.340];
% stored charge on plates, out dieletric in-between plates (nC)
Q2 = 220*[0, 0.059, 0.1372, 0.256, 0.319, 0.399, 0.468, 0.571, 0.645, 0.743, 0.783];

e = Q1*0.98e-2./(U*0.0531);
e_r = Q2./Q1;

p1 = polyfit(U, Q1, 1);
p2 = polyfit(U, Q2, 1);

Q1_fit = polyval(p1, U);
Q2_fit = polyval(p2, U);

figure;
plot(U, Q1, 'o', 'DisplayName', 'Q1 points', 'LineWidth', 2, 'Color', 'b');
hold on;
plot(U, Q2, 'x', 'DisplayName', 'Q2 points', 'LineWidth', 2, 'Color', 'b');

plot(U, Q1_fit, '--', 'DisplayName', 'Q1', 'LineWidth', 1.25);
plot(U, Q2_fit, '--', 'DisplayName', 'Q2', 'LineWidth', 1.25);

xlabel('U (kV)'); ylabel('Q (nC)');
title('Plot of U vs Q');
legend show;

grid on; grid minor;
hold off;

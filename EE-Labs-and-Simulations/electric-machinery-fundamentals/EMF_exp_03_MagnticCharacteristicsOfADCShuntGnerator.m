clear; clc; close all;

% field current
I_f = [35, 42, 55, 70, 84, 94, 104, 112, 117, 126, 138];

% induced armature voltage when I_f rises
V_a_I_f_rise = [63, 75, 94, 112, 126, 135, 143, 148, 150, 155, 159];
% induced armature voltage when I_f falls
V_a_I_f_fall = [79, 92, 111, 128, 141, 147, 152, 154, 156, 158, 159];

% plotting the data between 'I_f' and 'V_a'
figure;
plot(I_f, V_a_I_f_fall, '-.x', 'DisplayName', '{V_{a} when I_{f} fall}', ...
    'LineWidth', 1.5);
hold on;
plot(I_f, V_a_I_f_rise, '-.x', 'DisplayName', '{V_{a} when I_{f} rise}', ...
    'LineWidth', 1.5);

xlabel('I_f (Amps)'); ylabel('V_a (Volts)');
title('Graph between I_f and V_a');
legend show;
grid on;  grid minor;
hold off;

clear; clc; close all;

% RC
R1 = 1e3; C1 = 0.01e-6;
num1 = 1/(R1*C1); den1 = [1 1/(R1*C1)]; H1 = tf(num1, den1);

% RL
R2 = 500; L2 = 270e-6;
num2 = R2/L2; den2 = [1 R2/L2]; H2 = tf(num2, den2);

% RLC
R3 = 1e3; L3 = 10e-3; C3 = 0.1e-6;
num3 = 1/(L3*C3); den3 = [1 R3/L3 1/(L3*C3)]; H3 = tf(num3, den3);

%% cutoff Frequencies
fc1 = 1 / (2 * pi * R1 * C1);
fprintf('The cutoff frequency fc of RC filter is: %.2f Hz\n', fc1);

fc2 = R2 / (2 * pi * L2);
fprintf('The cutoff frequency fc of RL filter is: %.2f Hz\n', fc2);

fc3 = 1 / (2 * pi * sqrt(L3 * C3));
fprintf('The cutoff frequency fc of RLC filter is: %.2f Hz\n', fc3);

% band width
BW3 = R3 / (2 * pi * L3);
fprintf('The 3dB Bandwidth is: %.2f Hz\n', BW3);

%% Bode plot
figure;
bode(H1); hold on; bode(H2); bode(H3);
title('Bode Plot of Filters');
legend('RC', 'RL', 'RLC');
%set(gca, 'XScale', 'log'); xlim([10^2 10^9])
grid on; hold off;

%% Impulse Response
figure;
subplot(1,3,1); impulse(H1); title('Impulse Response of RC filter'); grid on;
subplot(1,3,2); impulse(H2); title('Impulse Response of RL filter'); grid on;
subplot(1,3,3); impulse(H3); title('Impulse Response of RLC filter'); grid on;

%% Step Response
figure;
subplot(1,3,1); step(H1); title('Step Response of RC filter'); grid on;
subplot(1,3,2); step(H2); title('Step Response RL filter'); grid on;
subplot(1,3,3); step(H3); title('Step Response of RLC filter'); grid on;

%% Pole-Zero Map
figure;
pzmap(H1); hold on; pzmap(H2); pzmap(H3);
title('Pole-Zero Map of Filters');
legend('RC', 'RL', 'RLC');
grid on; grid minor; hold off;

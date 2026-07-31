clear; clc; close all;

% parameters
R = 1000;       % resistance in ohms
L = 4.7e-3;     % inductance in henries
V0 = 2.5;       % amplitude of square wave voltage in volts
T = 47e-6;      % period of square wave in seconds
t_end = 94e-6;  % simulation time (to observe several cycles)
tau = L / R;    % time constant of RL circuit

t = 0:1e-6:t_end;

% square wave voltage input
V = V0 * square(2 * pi * t / T);

I = zeros(size(t)); V_R = zeros(size(t)); V_L = zeros(size(t));

I_prev = 0;

for i = 2:length(t)
    dt = t(i) - t(i-1);
    I(i) = I_prev + (V(i-1) - R * I_prev) * (dt / L);
    I_prev = I(i);
    V_R(i) = R * I(i);
    V_L(i) = L * (I(i) - I(i-1)) / dt;
end

fig = figure('Name', 'Series RL circuit response', 'NumberTitle', 'off');

subplot(2,2,1);
plot(t, V, 'LineWidth', 1.5);
title('V_{in}'); xlabel('Time (s)'); ylabel('Voltage (V)');
grid on; grid minor;

subplot(2,2,2);
plot(t, V_L, 'LineWidth', 1.5);
title('V_L'); xlabel('Time (s)'); ylabel('Voltage (V)');
grid on; grid minor;

subplot(2,2,3);
plot(t, V_R, 'LineWidth', 1.5);
title('V_R'); xlabel('Time (s)'); ylabel('Voltage (V)');
grid on; grid minor;

subplot(2,2,4);
plot(t, I, 'LineWidth', 1.5);
title('I'); xlabel('Time (s)'); ylabel('Current (A)');
grid on; grid minor;

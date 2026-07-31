clear; clc; close all;

% parameters
R = 1000;       % resistance in ohms (1 kΩ)
C = 0.01e-6;    % capacitance in farads (10 µF)
V0 = 2.5;       % amplitude of square wave voltage in volts (2.5 V)
T = 1e-4;       % period of square wave in seconds (100 µs)
t_end = 2e-4;   % simulation time (to observe several cycles) (200 µs)
tau = R * C;    % time constant of RC circuit

% time vector
t = 0:1e-6:t_end;  % time vector with a resolution of 1 microsecond

% square wave voltage input
V_in = V0 * square(2 * pi * t / T);

V_C = zeros(size(t)); V_R = zeros(size(t)); I = zeros(size(t));    

V_C_prev = 0;

% loop over time to compute the voltage and current response
for i = 2:length(t)
    dt = t(i) - t(i-1);
    I(i) = (V_in(i-1) - V_C_prev) / R;
    V_C(i) = V_C_prev + I(i) * dt / C;
    V_R(i) = R * I(i);
    V_C_prev = V_C(i);
end

fig = figure('Name', 'Series RC circuit response', 'NumberTitle', 'off');

subplot(2,2,1);
plot(t, V_in, 'LineWidth', 1.25);
title('V_{in}'); xlabel('Time (ms)'); ylabel('Voltage (V)');
grid on; grid minor;

subplot(2,2,2);
plot(t, V_C, 'LineWidth', 1.25);
title('V_C'); xlabel('Time (ms)'); ylabel('Voltage (V)');
grid on; grid minor;

subplot(2,2,3);
plot(t, V_R, 'LineWidth', 1.25);
title('V_R)'); xlabel('Time (ms)'); ylabel('Voltage (V)');
grid on; grid minor;

subplot(2,2,4);
plot(t, I, 'LineWidth', 1.25);
title('I'); xlabel('Time (ms)'); ylabel('Current (A)');
grid on; grid minor;

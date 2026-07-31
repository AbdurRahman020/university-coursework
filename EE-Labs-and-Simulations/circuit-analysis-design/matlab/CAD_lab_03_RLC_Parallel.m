clear; clc; close all;

% parameters
R = 1e3;                % resistance in ohms
L = 10e-3;              % inductance in henries
C = 0.012e-6;           % capacitance in farads
Vin = 5;                % input voltage in volts
f = 20e3;           % single frequency in Hz

omega = 2*pi*f;         % angular frequency
t = 0: 0.1/omega: 2/f;  % time vector

% admittance and current
Y = 1 / R + 1j * (omega * C - 1 / (omega * L));
I = Vin * Y;

% currents through components
i_R = Vin / R * cos(omega * t);
i_L = Vin / (omega * L) * sin(omega * t);
i_C = Vin * omega * C * - sin(omega * t);
% total current
i_T = i_R + i_L + i_C;

figure('Name', 'Parallel RLC circuit response', 'NumberTitle', 'off');

subplot(2,2,1);
plot(t, i_R, 'r'); grid on; grid minor;
title('Current through Resistor'); xlabel('Time (s)'); ylabel('I_R (A)');

subplot(2,2,2);
plot(t, i_L, 'g'); grid on; grid minor;
title('Current through Inductor'); xlabel('Time (s)'); ylabel('I_L (A)');

subplot(2,2,3);
plot(t, i_C, 'b'); grid on; grid minor;
title('Current through Capacitor'); xlabel('Time (s)'); ylabel('I_C (A)');

subplot(2,2,4);
plot(t, i_T, 'm'); grid on; grid minor;
title('Total Current in Circuit'); xlabel('Time (s)'); ylabel('I_T (A)');

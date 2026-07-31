clear; clc; close all;

% Parameters
R = 1e3;              % resistance in ohms
L = 10e-3;            % inductance in henries
C = 0.012e-6;         % capacitance in farads
Vin = 5;              % input voltage in volts
f = 000007e3;         % single frequency in Hz

omega = 2*pi*f;       % angular frequency
t = 0:0.01/omega:2/f; % time vector

% impedance and current
Z = R + 1j * (omega * L - 1 / (omega * C));
I = Vin / Z;

% current through the circuit
i_t = abs(I) * cos(omega * t + angle(I));

% voltages across components
v_R = abs(I) * R * cos(omega * t + angle(I));
v_L = abs(I) * omega * L * -sin(omega * t + angle(I));
v_C = abs(I) / (omega * C) * sin(omega * t + angle(I));
v_t = v_R + v_L + v_C;

figure('Name', 'Series RLC circuit response', 'NumberTitle', 'off');

subplot(2,2,1);
plot(t, v_R, 'r'); grid on; grid minor;
title('Voltage across Resistor'); xlabel('Time (s)'); ylabel('V_R (V)');

subplot(2,2,2);
plot(t, v_L, 'g'); grid on; grid minor;
title('Voltage across Inductor'); xlabel('Time (s)'); ylabel('V_L (V)');

subplot(2,2,4);
plot(t, v_C, 'b'); grid on; grid minor;
title('Voltage across Capacitor'); xlabel('Time (s)'); ylabel('V_C (V)');

subplot(2,2,3);
plot(t, v_t, 'm'); grid on; grid minor;
title('V_R + V_L + V_C'); xlabel('Time (s)'); ylabel('V_T (V)');

clear; clc; close all;

% RLC filter parameters
R = 1e3; L = 10e-3; C = 0.1e-6;
% transfer function
num = 1/(L*C); den = [1, R/L, 1/(L*C)]; H = tf(num, den);

%% calculations

% input signal Vin(t) = 5*cos(200*pi*t + pi/6)
omega = 2 * pi * 100; Vin_amp = 5;  Vin_phase = pi/6; 

% frequency response at the input frequency (f_in = 100 Hz)
[mag_in, phase_in] = bode(H, omega);
phase_in_rad = deg2rad(phase_in);

% output signal: Vout(t) = Vin_amp * |H(jω)| * cos(ωt + φ_in + <H(jω))
Vout_amp = Vin_amp * mag_in;
Vout_phase = Vin_phase + phase_in_rad;

t = 0:1e-5:0.03;

Vin = Vin_amp * cos(omega * t + Vin_phase);
Vout = Vout_amp * cos(omega * t + Vout_phase);

%% display input and output signals

fprintf('Input Voltage Vin(t) = %.2f*cos(200*pi*t + %.2f rad)\n', Vin_amp, Vin_phase);
fprintf('Output Voltage Vout(t) = %.4f*cos(200*pi*t + %.4f rad)\n', Vout_amp, Vout_phase);

%% plot input and output signals

figure;
plot(t*1000, Vin, 'b'); hold on; plot(t*1000, Vout, 'r--');
grid on; grid minor;
xlabel('Time (ms)'); ylabel('Voltage (V)');
title('Input and Output Voltages of RLC Filter');
legend('V_{in}(t)', 'V_{out}(t)');

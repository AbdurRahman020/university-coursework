clc; clear; close all;

%% Machine specifications

% supply frequency in Hz
f = 50;
% number of poles
P = 4;
% synchronous speed (RPM)
ns = 120*f/P;
% synchronous angular speed (rad/s)
ws = 2*pi*f;

%% No-Load Test Inputs

% line voltage (V)
V_L = 400;
% no-load current (A)
I_0 = 4.2;
% no-load power (W)
P_0 = 420;

% phase voltage
V_ph = V_L/sqrt(3);
% phase power
P_ph = P_0/3;
% core loss resistance
R_c = V_ph^2/P_ph;
% magnetizing current
I_m = sqrt(I_0^2 - (V_ph/R_c)^2);
% magnetizing reactance
X_m = V_ph/I_m;

fprintf('Xm = %.2f ohms\n', X_m);

%% Locked Rotor Test Inputs

% locked rotor voltage (V)
V_LR = 120;
% locked rotor current (A)
I_LR = 15;
% locked rotor power (W)
P_LR = 1800;

V_ph_LR = V_LR/sqrt(3);
P_ph_LR = P_LR/3;
% equivalent resistance
R_eq = P_ph_LR/(I_LR^2);
% equivalent impedance
Z_eq = V_ph_LR/I_LR;
% equivalent reactance
X_eq = sqrt(Z_eq^2 - R_eq^2);

% assuming rotor and stator equal division
R1 = R_eq/2;
R2 = R_eq/2;
X1 = X_eq/2;
X2 = X_eq/2;

fprintf('R1 = %.2f, X1 = %.2f, R2 = %.2f, X2 = %.2f\n', R1, X1, R2, X2);

%% Classification using slip

% measured rotor speed (RPM)
nm = 1430;
% slip
s_test = (ns - nm)/ns;

if s_test > 0
    disp('Mode: Induction Motor');
elseif s_test == 0
    disp('Mode: Floating');
else
    disp('Mode: Induction Generator');
end

%% Torque-Speed Curve using Chapman Model

% slip range from 0.001 to 1
s = linspace(0.001,1,500);
% thevenin impedance
Z_th = (1j*X_m*(R1 + 1j*X1)) / (R1 + 1j*(X1 + X_m));
% thevenin voltage
V_th = V_ph*(1j*X_m)/(R1 + 1j*(X1 + X_m));
R_th = real(Z_th);
X_th = imag(Z_th);

% torque equation
T = (3*(abs(V_th)^2).*(R2./s)) ./ (ws*((R_th + R2./s).^2 + (X_th + X2).^2));
% rotor speed in RPM
n = (1 - s)*ns;

%% Plot Torque-Speed Curve

plot(n, T, 'LineWidth', 2);
xlabel('Speed (RPM)'); ylabel('Torque (Nm)');
title('Torque-Speed Curve (Chapman Induction Motor Model)');
grid on; grid minor;

% correct x-axis: from 0 to synchronous speed
xlim([0 ns]);
% optional: small margin above max torque
ylim([0 max(T)*1.1]);

fprintf('Synchronous Speed = %d RPM\n', ns);

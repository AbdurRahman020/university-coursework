clear; clc; close all;

% parameters
R1 = 100; R2 = 100; C = 10e-6; L = 0.1;

% initial conditions
V_C_0 = -5; I_L_0 = 0;

syms s t

% impedance in s-domain
Z_L = s * L; Z_C = 1 / (s * C);

% current through the circuit
I_s = -(V_C_0 / s)/(R1 + R2 * Z_L / (R2 + Z_L) + Z_C);

i_t = ilaplace(I_s,s,t);

% node voltages
V_A_s = I_s * R1; V_B_s = -I_s * R2 * Z_L / (R2 + Z_L);

% voltage across capacitor
V_C_s = - V_A_s + V_B_s;

% inverse laplace transform
V_A_t = ilaplace(V_A_s, s, t);
V_B_t = ilaplace(V_B_s, s, t);
V_C_t = ilaplace(V_C_s, s, t);

t = [0, 0.015];

figure;
fplot(V_A_t, t, 'r', 'LineWidth', 1.25); hold on;
fplot(V_B_t, t, 'g', 'LineWidth', 1.25);
fplot(V_C_t, t, 'b', 'LineWidth', 1.25);

title('Task 2'); xlabel('time (s)'); ylabel('voltage (V)');
legend('v_A(t)', 'v_B(t)', 'v_C(t)');
grid on; grid minor; hold off;

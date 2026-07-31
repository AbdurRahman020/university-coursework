clear; clc; close all;

% given parameters
R1 = 500; R2 = 500; R3 = 1e3; L = 0.5; C = 0.2e-6; V_A = 15; 

syms s t

% initial capacitor voltage and inductor current
V_C_0 = 15; I_L_0 = 0;

% impedances in s-domain
Z_L = s * L; Z_C = 1 / (s * C);

% indcutor current in laplace domain
I_L_s = (- V_C_0 / s)/(R2 + R3 + Z_L + Z_C);

% inverse laplace transform to get i_L(t)
i_L_t = ilaplace(I_L_s, s, t);

figure;
fplot(i_L_t, [0, 0.01]); grid on; grid minor;

title('Inductor Current i_L(t)');
xlabel('t (s)'); ylabel('i_L(t) (A)');

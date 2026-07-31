clc; clear; close all;

syms t s I1_s I2_s

% parameters
R1 = 1e3; R2 = 1e3; R3 = 2e3; L = 1; C = 0.1e-6; V_in_s = 5 / (s + 2000);
% initial conditions
i_L_0 = 10e-3; v_C_0 = 10;

% impedances in s-domain
Z_L = s * L; Z_C = 1 / (s * C);

% mesh equations
eq1 = I1_s*(R1 + R2 + Z_L) - I2_s*(R2 + Z_L) + V_in_s + L*i_L_0 == 0;
eq2 = -I1_s*(R2 + Z_L) + I2_s*(R2 + Z_L + R3 + Z_C) - v_C_0/s - L*i_L_0 == 0;

% getting I1_(s) and I2(s) 
sol = solve([eq1, eq2], [I1_s, I2_s]);

disp('I2(s) = '); pretty(sol.I2_s)

% voltage accros capacitor
V_C_s = - sol.I2_s * Z_C + v_C_0/s;

% inverse Laplace transform of V_C(s) and V_in(s)
v_C_t = ilaplace(V_C_s, s, t); v_in_t = ilaplace(V_in_s, s, t);

t = [0, 0.005];

% plots
figure;
fplot(v_C_t, t, 'LineWidth', 1.25); hold on; 
fplot(v_in_t, t, 'LineWidth', 1.25);

title('Task 3'); xlabel('time (s)'); ylabel('voltage (V)');
legend('v_C(t)', 'v_{in}(t)');
grid on; grid minor; hold off;

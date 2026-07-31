clear; clc; close all;

% parameters
R = 1e3;              % resistance in ohms
L = 10e-3;            % inductance in henries
C = 0.012e-6;         % capacitance in farads

% frequency range for the plot
f_range = logspace(2, 6, 500);  % frequencies from 100 Hz to 1 MHz
omega_range = 2*pi*f_range;

Z = zeros(size(f_range));

% calculate impedance for each frequency
for i = 1:length(f_range)
    Z(i) = R + 1j * (omega_range(i) * L - 1 / (omega_range(i) * C));
end

% resonant frequency calculation
f_r = 1 / (2 * pi * sqrt(L * C));

figure('Name', 'Series RLC', 'NumberTitle', 'off');
loglog(f_range, abs(Z), 'b');
grid on; grid minor; hold on;

xline(f_r, 'r--', ['f_0 = ' num2str(f_r, '%.2f') ' Hz'], 'LabelHorizontalAlignment', 'left');

title('Z vs f for Series RLC Circuit');
xlabel('f (Hz)'); ylabel('Z (\Omega)');
legend('Impedance', 'Resonant Frequency');
hold off;

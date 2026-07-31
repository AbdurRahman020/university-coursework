clear; clc; close all;

% parameters 
R = 1e3; L = 10e-3; C = 0.1e-6; Vin = 5;
% time vector
t = 0:1e-6:1e-3;
% frequencies
freqs = [2e3, 5e3, 8e3];

vr = zeros(length(freqs), length(t));
vl = zeros(length(freqs), length(t));
vc = zeros(length(freqs), length(t));
v = zeros(length(freqs), length(t));

for i = 1:length(freqs)
    f = freqs(i); omega = 2*pi*f;
    Z = R + 1i*(omega*L - 1/(omega*C));
    I = Vin / Z;

    vr(i,:) = abs(I) * R * cos(omega * t + angle(I));
    vl(i,:) = abs(I) * omega * L * -sin(omega * t + angle(I));
    vc(i,:) = abs(I) / (omega * C) * sin(omega * t + angle(I));

    v(i,:) = vr(i,:) + vl(i,:) + vc(i,:);
end

% V_R at diffrenet frequencies 
figure;
subplot(2,2,1);
hold on;
plot(t, vr(1,:), 'r', 'DisplayName', 'V_R at 2 kHz');
plot(t, vr(2,:), 'g', 'DisplayName', 'V_R at 5 kHz');
plot(t, vr(3,:), 'b', 'DisplayName', 'V_R at 8 kHz');
title('V_R for 2 kHz, 5 kHz, and 8 kHz');
xlabel('t (s)'); ylabel('V_R (V)');
legend; grid on; grid minor;  hold off;

% V_L at diffrenet frequencies
subplot(2,2,2);
hold on;
plot(t, vl(1,:), 'r', 'DisplayName', 'V_L at 2 kHz');
plot(t, vl(2,:), 'g', 'DisplayName', 'V_L at 5 kHz');
plot(t, vl(3,:), 'b', 'DisplayName', 'V_L at 8 kHz');
title('V_L for 2 kHz, 5 kHz, and 8 kHz');
xlabel('t (s)'); ylabel('V_L (V)');
legend; grid on; grid minor; hold off;

% V_C at diffrenet frequencies
subplot(2,2,3);
hold on;
plot(t, vc(1,:), 'r', 'DisplayName', 'V_C at 2 kHz');
plot(t, vc(2,:), 'g', 'DisplayName', 'V_C at 5 kHz');
plot(t, vc(3,:), 'b', 'DisplayName', 'V_C at 8 kHz');
title('V_C for 2 kHz, 5 kHz, and 8 kHz');
xlabel('t (s)'); ylabel('V_C (V)');
legend; grid on; grid minor;  hold off;

% V_R + V_L + V_C = V_in at diffrenet frequencies
subplot(2,2,4)
hold on;
plot(t, v(1,:), 'r', 'DisplayName', 'V_{in} at 2 kHz');
plot(t, v(2,:), 'g', 'DisplayName', 'V_{in} at 5 kHz');
plot(t, v(3,:), 'b', 'DisplayName', 'V_{in} at 8 kHz');
title('V_{in} for 2 kHz, 5 kHz, and 8 kHz');
xlabel('t (s)'); ylabel('V_{in} (V)');
legend; grid on; grid minor; hold off;

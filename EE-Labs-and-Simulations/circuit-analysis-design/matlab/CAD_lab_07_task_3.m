clear; clc; close all;

% RC filter parameters
R1 = 1e3; C = 0.01e-6; num_RC = 1/(R1*C); den_RC = [1 1/(R1*C)];
% RL filter
R2 = 500; L = 270e-6; num_RL = R2/L; den_RL = [1 R2/L];

% multiplying numerators (of RL and RC) and denominators (of RL and RC)
num = num_RC*num_RL; den = conv(den_RC, den_RL); 

% final transfer function(s)
H_convo = tf(num, den); % with buffer between each stage
H_actual = tf(num, den + [0 0 1/(L*C)]); % no buffer

disp('Transfer Function H(s):'); H_convo
disp('Transfer Function H(s):'); H_actual

%% Bode plot
figure;
subplot(1,2,1); bode(H_convo); title('Bode Plot via H_{convo}'); grid on; 
subplot(1,2,2); bode(H_actual); title('Bode Plot via H_{actual}'); grid on;

%% Frequency response

[mag1, phase1, w1] = bode(H_convo);
% converting into mag into dB
mag1_dB = 20*log10(mag1(:));
% finding index where mag_dB is less than -3dB
idx1 = find(mag1_dB <= -3, 1);
f1_cutoff = w1(idx1)/(2*pi);

fprintf('Cutoff frequency for H_convo: %.2f Hz\n', f1_cutoff);

[mag2, phase2, w2] = bode(H_actual);
% converting into mag into dB
mag2_dB = 20*log10(mag2(:));
% finding index where mag_dB is less than -3dB
idx2 = find(mag2_dB <= -3, 1);
f2_cutoff = w2(idx2)/(2*pi);

fprintf('Cutoff frequency for H_actual: %.2f Hz\n', f2_cutoff);

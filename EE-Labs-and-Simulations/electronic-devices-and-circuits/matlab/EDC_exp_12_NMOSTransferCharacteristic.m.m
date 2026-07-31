ID = [0.42 0.44 0.47 0.48 0.521 0.544];  % mA
%VD = [2.02 2.02 2.02 2.02 2.02 2.02];    % V
VGS = [0.7 0.8 0.9 1.0 1.1 1.2];         % V

% fit a 2nd order polynomial: ID = a*VGS^2 + b*VGS + c
p = polyfit(VGS, ID, 2);

% generate fitted curve
VGS_fit = linspace(min(VGS), max(VGS), 100);
ID_fit = polyval(p, VGS_fit);

% plot
figure
plot(VGS, ID, 'x', 'MarkerSize', 8, 'LineWidth', 2, 'DisplayName', 'Measured Data')
hold on
plot(VGS_fit, ID_fit, '-.', 'LineWidth', 2, 'DisplayName', 'Fitted Curve')

xlabel('V_{GS} (V)'); ylabel('I_D (mA)')
title('NMOS I_D vs V_{GS} Characteristics (V_D = 2V)')
legend('Location', 'best')
grid on; grid minor;
hold off;

% display the fitted equation
fprintf('Fitted equation: I_D = %.4f*V_{GS}^2 + %.4f*V_{GS} + %.4f\n', p(1), p(2), p(3));

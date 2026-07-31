% Given Data
T = 25:5:70;

CuNi = [172, 173, 173, 171.6, 171.7, 171.6, 171.3, 172, 174, 175];
C = [1002, 1003, 1001, 1011, 1000, 1011, 1009, 1000, 1000, 1000];
Met = [997, 1000, 991, 983, 960, 963, 964, 956, 959, 954];
NTC = [966, 781, 669, 525, 447, 378, 317, 280, 243, 214];
PTC = [56.4, 61.7, 67.9, 79.7, 95, 121.4, 165, 258, 462, 890];

% Reference and final temperatures
T1 = 25;
T2 = 70;

% Calculate alpha (temperature coefficient of resistance) for each material
alpha_CuNi = (CuNi(end) - CuNi(1)) / (CuNi(1) * (T2 - T1));
alpha_C = (C(end) - C(1)) / (C(1) * (T2 - T1));
alpha_Met = (Met(end) - Met(1)) / (Met(1) * (T2 - T1));
alpha_NTC = (NTC(end) - NTC(1)) / (NTC(1) * (T2 - T1));
alpha_PTC = (PTC(end) - PTC(1)) / (PTC(1) * (T2 - T1));

% Display Results
disp('Temperature Coefficient of Resistance (alpha) for each material:');
fprintf('CuNi: %.6f\n', alpha_CuNi);
fprintf('C: %.6f\n', alpha_C);
fprintf('Met: %.6f\n', alpha_Met);
fprintf('NTC: %.6f\n', alpha_NTC);
fprintf('PTC: %.6f\n', alpha_PTC);

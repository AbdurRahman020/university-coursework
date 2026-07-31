clear; clc; close all;

% the frequency vectors
f_at_1x = 10:10:100;           
f_at_10x = 100:100:1000;        
f_at_100x = 1000:1000:10000;     
f_at_1kx = 10000:10000:100000;    
f_at_10kx = 100000:100000:1000000; 

freq = {f_at_1x, f_at_10x, f_at_100x, f_at_1kx, f_at_10kx};

% the current vectors
i_at_1x = {0.0, 0.0, 0.0, 0.01, 0.01, 0.02, 0.02, 0.03, 0.04, 0.04};
i_at_10x = {0.04, 0.11, 0.18, 0.25, 0.31, 0.38, 0.45, 0.52, 0.58, 0.64};
i_at_100x = {0.64, 1.28, 1.86, 2.37, 2.79, 3.14, 3.44, 3.65, 3.82, 3.95};
i_at_1kx = {3.95, 4.0, 3.18, 2.25, 1.36, 0.73, 0.38, 0.22, 0.14, 0.09};
i_at_10kx = {0.10, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};

i = {i_at_1x, i_at_10x, i_at_100x, i_at_1kx, i_at_10kx};

% matrix names for legend
matrix_names = {'f (1x)', 'f (10x)', 'f (100x)', 'f (1kx)', 'f (10kx)'};

figure;
hold on;

for j = 1:length(freq)
    freq_values = freq{j};
    i_values = cell2mat(i{j});
    
    plot(log10(freq_values), i_values, 'DisplayName', matrix_names{j}, ...
         'LineWidth', 1.5, 'Marker', 'o', 'MarkerSize', 5);
end

xlabel('log_{10}(freq)'); ylabel('i (mA)');
title('Log Frequency vs Current');
xlim([1 log10(1e6)]);
grid on;

ax = gca;  
ax.GridAlpha = 0.5;  
ax.MinorGridAlpha = 0.3;  
ax.XMinorGrid = 'on';  ax.YMinorGrid = 'on';  
legend('show');
hold off;

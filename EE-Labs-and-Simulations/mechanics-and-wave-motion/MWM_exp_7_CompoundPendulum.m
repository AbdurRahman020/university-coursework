clear; clc; close all;

% data
X_A = [45, 40, 35, 30, 25, 20, 15, 10, 5]; 
t_A = [1.616, 1.5805, 1.548, 1.5165, 1.5335, 1.5855, 1.6875, 1.933, 2.684];  

X_B = [-45, -40, -35, -30, -25, -20, -15, -10, -5]; 
t_B = [1.6145, 1.5825, 1.548, 1.5145, 1.530, 1.5855, 1.6855, 1.9325, 2.667];  

% create the figure
figure;  
hold on;  

% plot the data
plot(X_B, t_B, 'b', 'DisplayName', 't_B');  
plot(X_A, t_A, 'r', 'DisplayName', 't_A');  

% define the horizontal lines
t_lines = [1.54, 1.6];  
yline(t_lines(1), 'm', 't = 1.54', 'DisplayName', 't = 1.54');  
yline(t_lines(2), 'm', 't = 1.6', 'DisplayName', 't = 1.6');  

% set plot limits and labels
xlim([-50 50]);  
xlabel('X (cm)');   ylabel('t (sec)');  
title('Graph between distance from Centre of Gravity and Time Period');  
legend('show');  
grid on;  

% adjust grid properties
ax = gca;  
ax.GridAlpha = 0.5;  
ax.MinorGridAlpha = 0.3;  
ax.XMinorGrid = 'on';  ax.YMinorGrid = 'on';  

% find all intersections for each t_line
for t_line = t_lines
    % find intersections for t_A
    X_intersect_A = find_intersections(X_A, t_A, t_line);
    for X_val = X_intersect_A
        fprintf('Intersection for t = %.2f with t_A: X = %.2f\n', t_line, X_val);
    end
    
    % find intersections for t_B
    X_intersect_B = find_intersections(X_B, t_B, t_line);
    for X_val = X_intersect_B
        fprintf('Intersection for t = %.2f with t_B: X = %.2f\n', t_line, X_val);
    end
end

hold off;

% function to find intersections
function X_intersects = find_intersections(X, t, t_line)
    X_intersects = [];
    for i = 1:length(t)-1
        % check if t_line is between the current and next t value
        if (t(i) < t_line && t(i+1) > t_line) || (t(i) > t_line && t(i+1) < t_line)
            % linear interpolation to find the intersection point
            x_intersect = X(i) + (X(i+1) - X(i)) * (t_line - t(i)) / (t(i+1) - t(i));
            % store the intersection
            X_intersects(end + 1) = x_intersect;
        end
    end
end

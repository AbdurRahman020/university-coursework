clear; clc; close all;

t = 0:0.1:10;
v1 = 5*cos(2*t + 0.7854);
t_axis = 1e-8*t;

plot(t, t_axis, 'w', t, v1, 'r');

grid on; grid minor; hold on;

v2 = 2*exp(-t);
plot(t, v2, 'g');

v3 = 10*exp(-t/2).*cos(2*t + 0.7854);
plot(t, v3, 'b');

title('Example 1 -- Plot of {v_1}(t), {v_2}(t) and {v_3}(t)');
xlabel('t (s)'); ylabel('v(t) (V)')
text(6, 6, '{v_1}(t)'); text(4.25, -1.25, '{v_2}(t)'); text(1, 1.75, '{v_3}(t)');

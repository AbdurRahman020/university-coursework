clear; clc; close all;

syms t;
f = cos(5000*t);

F = laplace(f); pretty(F)

f_i = ilaplace(F); pretty(f_i)

sys = tf([1, 0], [1, 0, 25000000]);

pzmap(sys)

grid on;

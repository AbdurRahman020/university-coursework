clear; clc; close all;

syms t;

% the given function
f = (500 + 100*exp(-500*t)*t*sin(1000*t))*heaviside(t);

% laplace transform
F = laplace(f);
pretty(F)

% inverse laplace transform
f_i = ilaplace(F);
pretty(f_i) 

% extracting numerator an denumerator polynomials
[num, den] = numden(F);

% transfer function
sys = tf(sym2poly(num), sym2poly(den))

% poles zeros map
pzmap(sys)

grid on;

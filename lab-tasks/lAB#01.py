"""
LAB # 01: Implementation of PRINT Statement and Arithmetic Operations in PYTHON
"""

import math

# %% Q#2: Finding & Eliminating Syntax Errors

print("Welcome to Intro to Computing")
print("Nice to meet you")

# %% Q#3: Print and Flowchart

print('My name is ALi')
print('I scored 1000/1100 marks in FSc')
print('and 380/400 in entry test.')

# %% Q#4: Printing Diamonds

print("A Dimond\n")

# Part A:
print("  *  ")
print(" *** ")
print("*****")
print(" *** ")
print("  *  ")

# Part B:
print('  *  \n *** \n*****\n *** \n  *  ')

# %% Q#5: Basic Arithmetic Operations

a, b, c = 3, 1, -2

r1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
r2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

print(f"The roots are {r1} and {r2}")

# %% Q#6: Trigonometric Operations

A, C = 50, 10

alpha = math.acos(C/A)
B = C * math.tan(a)

print(f"The value of variable alpha is {alpha * (180/math.pi)} degrees")
print(f"The value of b is {B} meters")

# %% Q#7: Trigonometry

a, b, c, d, theta = 10, 5, 15, 20, 45
theta = theta*(math.pi/180)

num = math.sqrt((a/b * math.sin(theta))**(a/b**2) +
                (b/a * math.cos(theta))**(1/(a+b)))
den = c * math.tan(theta) - d/c

frac = num/den

print(f"The answer is {frac}")

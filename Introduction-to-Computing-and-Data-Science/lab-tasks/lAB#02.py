"""
LAB # 02: Implementation of Functions, Comparison and Logical Operators in Python
"""

# %% Q#2: Prompting And Logical Comparison

import math
math_marks = int(input("Enter the marks in Maths: "))
urdu_marks = int(input("Enter the marks in Urdu: "))

print(math_marks >= 5 and urdu_marks < 3)

# %% Q#3: Prompting And String Comparison

correct_password = "uet@ 2024"
input_password = input("Enter the password: ")

print(correct_password == input_password)

# %% Q#4: Determining The Data Type

x = 1.5
is_int = type(x) is int

print(f"For x = {x} the answer is {is_int}")

# %% Q#5: Floating Number Comparison

s = 0.1 + 0.1 + 0.1

print(s)  # s = 0.30000000000000004 why?
# Reason: In computers, the issue arises from how floating-point numbers are
# represented in binary. The number 0.1 cannot be represented exactly in binary
# floating-point, leading to small precision errors in arithmetic calculations.

print(s == 0.3)  # comparison evalutes to False

# %% Q#6: Boolean Statements

ali, umar, salman = True, True, True
happy_or_not = (ali or umar) and not salman

print(f"For ali = {ali}, umar = {umar} and salman = {salman},\
 the answer is \n{happy_or_not}")

# %% Q#8: User-Defined Function (No Argument, No Return Value)


def foo():
    print("My name is Ali")
    print("I scored 1000/1100 marks in FSc")
    print("and 380/400 in the entry test.")


foo()

# %% Q#9: User-Defined Function (With Integer Arguments & Floating-Point Return Values)


def CalculateRoots(a, b, c):
    r1, r2 = (-b + math.sqrt(b**2 - 4*a*c)) / \
        (2*a), (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    return r1, r2


root1, root2 = CalculateRoots(3, 1, -2)

print(f"The roots are {root1} and {root2}")

"""
LAB # 03: Implementation of Conditional Statements & Lambda Functions in Python
"""

# %% Q#2: Errors

x = 4

if x % 2 == 0:
    print('The number is even')
else:
    print("The number is odd")

# %% Q#3: Writing Program Using Pseudo-Code

x = float(input("Eneter a number: "))

if x > 15:
    print("The grade is A")
elif x > 10 and x <= 15:
    print("The grade is B")
else:
    print("Invalid input")

# %% Q#4: Function (One Real Number Argument, No Return Value)


def absoulte(y):
    if y >= 0:
        return y
    else:
        return -y


# test cases
print(f"The absoulte value is {absoulte(-1.5)}")
print(f"The absoulte value is {absoulte(0)}")
print(f"The absoulte value is {absoulte(8)}")

# %% Q#5: Lambda Function & Tuples


def a(x, y): return (x + y, x - y)


b = a(5, 2)

print("The sum and the differnece is", b)
print("The sum is", b[0], "and the difference is", b[1])

# %% Q#6: Function (One Real Number Argument, String Return Value)


def foo(x):
    if x > 0:
        return "positive"
    elif x == 0:
        return "zero"
    else:
        return "negative"

# %% Q#7: Debugging The Code


def CalculateRoots(a, b, c):
    disc = b**2 - 4*a*c

    r1 = (-b + disc**0.5)/(2*a)
    r2 = (-b - disc**0.5)/(2*a)

    if disc > 0:
        print(f"for a = {a}, b = {b} and c = {
              c} The roots are real and distinct. r1 = {r1} and r2 = {r2}")
    elif disc == 0:
        print(f"for a = {a}, b = {b} and c = {
              c} The roots are real and equal. r1 = {r1} and r2 = {r2}")
    else:
        print(f"for a = {a}, b = {b} and c = {
              c} The roots are complex. r1 = {r1} and r2 = {r2}")


# test cases
CalculateRoots(3, 1, -2)
CalculateRoots(1/4, 5, 25)
CalculateRoots(1, 4, 5)

# %% Q#8: Function With String And Boolean Arguments


def r(x, y, z):
    if x == "and":
        return y and z
    elif x == "Nand":
        return not (y and z)


# test cases
print("The result is", r("and", True, True))
print("The result is", r("Nand", True, True))

"""
LAB EXAM #01
DATE: 15-NOV-2024
"""
# %% Q#01: Basic Arthmatics

from IPython import get_ipython
get_ipython().run_line_magic('reset', '-sf')

a, b = 1, 2

print(f"sum = {a + b}")
print(f"difference = {a - b}")
print(f"product = {a * b}")
print(f"division = {a/b}")

# %% Q#02: for loop

get_ipython().run_line_magic('reset', '-sf')

y = 8
for i in range(y):
    if i % 2 == 0:
        print(i)

# %% Q#03: List to String conversion with certain condition

get_ipython().run_line_magic('reset', '-sf')

L = [500, 35, -5, 25, -4]

for x in L:
    if 10 <= x <= 30:  # equivalent to: x >= 10 and x <= 30
        print('e')
    elif 31 <= x <= 50:  # equivalent to: x >= 31 and x <= 50
        print('f')
    elif x < 0:
        print('g')
    elif x == 500:
        print('h')

# %% Q#04: Sum, Lenght and In-Place List Modification

get_ipython().run_line_magic('reset', '-sf')


def f(L):
    # iterate over list via indexing
    for i in range(len(L)):
        # in-place modify the list elements
        L[i] *= 2
    return sum(L), len(L)


# original list
a = [5, 4, 1, 2, 3]
print(f'original list: {a}')

s, l = f(a)
print(f'sum of list elements = {s}\nno of list elements = {l}')

# list modification after calling the function 'f'
print(f'in-place modified list: {a}')

# %% Q#05: Sum of Digits using Remainder & Quotient

get_ipython().run_line_magic('reset', '-sf')


def f(d):
    s = 0
    while True:
        r, d = divmod(d, 10)
        s += r
        if d == 0:
            break
    return s


print(f(4224))
print(f(55555))

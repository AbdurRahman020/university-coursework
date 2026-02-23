"""
LAB # 12: Plotting Data + Iterators & Generators in Python
"""

import time
import numpy as np
import matplotlib.pyplot as plt

# %% Q#2 Generator


def three_flips(coin):
    coin_list = list(coin)
    for i in range(len(coin_list) - 2):
        yield ''.join(coin_list[i:i+3])


a = three_flips(iter('HTTHHT'))
print(next(a))
print(next(a))

# %% Q#3 Iterator


def count_occurances(t, n, x):
    count = 0
    for i in range(n):
        try:
            item = next(t)
            if item == x:
                count += 1
        except:
            StopIteration
            break
    return count


s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
print(count_occurances(s, 10, 9))

s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
print(count_occurances(s2, 3, 10))

s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
print(count_occurances(s, 1, 3))
print(count_occurances(s, 3, 2))
print(next(s))

s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
print(count_occurances(s2, 6, 6))

# %% Q#4


def foo(a, b):
    iter_a, iter_b = iter(a), iter(b)

    while True:
        try:
            yield next(iter_a)
        except StopIteration:
            pass

        try:
            yield next(iter_b)
        except StopIteration:
            pass


t = foo([1, 2], [3, 4])

print(next(t))  # 1
print(next(t))  # 2
print(next(t))  # 3
print(next(t))  # 4

# %% Q#5 Plotting the given graph

x1, y1 = [1, 3], [1, 3]
x2, y2 = [1, 3], [3, 1]

plt.figure()

plt.plot(x1, y1, linewidth=2, color='red', label='line 1')
plt.plot(x2, y2, linestyle=':', color='green', label='line 2')

plt.xlabel('Integers 1')
plt.ylabel('Integers 2')
plt.legend()

plt.grid()

plt.show()

# %% Q#6 Sinusoidal function plot


def Sine(A, f, p, ts, lbl, clr):
    t = np.linspace(0, ts, 1000)

    phi_rad = np.deg2rad(p)

    y = A * np.sin(2 * np.pi * f * t + phi_rad)

    plt.plot(t, y, label=lbl, color=clr)


def SetPlot(xlbl, ylbl, tit):
    plt.title(tit)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    plt.grid()
    plt.legend()


plt.figaspect(1)
Sine(5, 5, 0, 2, 'v1', 'red')
SetPlot('time', 'amplitude', 'Phase A')

# %% Q#7 Three Phase Voltage plot


fig, axs = plt.subplots(2, 3, figsize=(16, 9))
fig.subplots_adjust(hspace=0.25, wspace=0.25)

plt.sca(axs[0, 0])
Sine(5, 5, 0, 2, 'v1', 'red')
SetPlot('time', 'amplitude', 'Phase A')

plt.sca(axs[0, 1])
Sine(5, 5, 120, 2, 'v2', 'yellow')
SetPlot('time', 'amplitude', 'Phase B')

plt.sca(axs[0, 2])
Sine(5, 5, 240, 2, 'v3', 'green')
SetPlot('time', 'amplitude', 'Phase C')

plt.sca(axs[1, 0])
Sine(5, 5, 0, 2, 'v1', 'red')
Sine(5, 5, 120, 2, 'v2', 'yellow')
Sine(5, 5, 240, 2, 'v3', 'green')
SetPlot('time', 'amplitude', 'Phase A, B and C')

axs[1, 1].axis('off')
axs[1, 2].axis('off')

axs[1, 0].set_position([0.125, 0.1, 0.775, 0.355])

plt.show()

# %% Q#8 Two Cirlces plot


def PrintCircle(a, b, r, color, name):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = a + r * np.cos(theta)
    y = b + r * np.sin(theta)

    plt.plot(x, y, label=name, color=color)
    plt.scatter(a, b, color=color, zorder=5)
    plt.text(a, b, f"  ({a},{b})", fontsize=12,
             color=color, verticalalignment='bottom')


plt.figure(figsize=(6, 6))

PrintCircle(2, 15, 4, 'blue', 'circle 1')
PrintCircle(15, 15, 4, 'red', 'circle 2')

plt.title("Two circles with centers")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.legend()

plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.show()

# %% Q#10 Vectorization


st1 = time.time()
A1 = list(range(50000))
B1 = [3] * 50000
S1 = sum(A1[i] * B1[i] for i in range(len(A1)))
et1 = time.time()

print(f"sum S (calculated with lists and loop): {S1}")
print(f"execution time for part a: {et1 - st1:.5f} seconds")

st2 = time.time()
A2 = np.arange(50000, dtype=np.int64)
B2 = np.full(50000, 3, dtype=np.int64)
S2 = np.dot(A2, B2)
et2 = time.time()

print(f"sum S (calculated using numpy dot product): {S2}")
print(f"execution time for part b: {et2 - st2:.5f} seconds")

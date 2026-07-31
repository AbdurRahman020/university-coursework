'''
midterm exam question
'''

# from IPython import get_ipython
# get_ipython().run_line_magic('reset', '-sf')

# %%

L = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'],
     ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R'],
     ['S', 'T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

new_L = []

for _ in range(10):
    x = input('Enter a character (in range 0-9, A-Z): ').upper()
    if x in '0123456789':
        new_L.append(x)

    for i in range(len(L)):
        if x in L[i]:
            new_L.append(str(i+2))
            break

p1, p2, p3 = ''.join(new_L[0:3]), ''.join(new_L[3:6]), ''.join(new_L[6:10])
print(f"CODE = {p1}-{p2}-{p3}")

# %%

d = {
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R'],
    8: ['S', 'T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z']
}

new_L = []

for _ in range(10):
    x = input('Enter a character (in range 0-9, A-Z): ').upper()

    if x in '0123456789':
        new_L.append(x)
    else:
        for key, value in d.items():
            if x in value:
                new_L.append(str(key))
                break

p1 = ''.join(str(new_L[i]) for i in range(0, 3))
p2 = ''.join(str(new_L[i]) for i in range(3, 6))
p3 = ''.join(str(new_L[i]) for i in range(6, 10))

print(f"CODE = {p1}-{p2}-{p3}")

# %%

new_L = []

for _ in range(10):
    x = input('Enter a character (in range 0-9, A-Z): ').upper()

    if x.isdigit():
        new_L.append(x)
    elif x in 'ABC':
        new_L.append('2')
    elif x in 'DEF':
        new_L.append('3')
    elif x in 'GHI':
        new_L.append('4')
    elif x in 'JKL':
        new_L.append('5')
    elif x in 'MNO':
        new_L.append('6')
    elif x in 'PQRS':
        new_L.append('7')
    elif x in 'TUV':
        new_L.append('8')
    elif x in 'WXYZ':
        new_L.append('9')

p1, p2, p3 = ''.join(new_L[0:3]), ''.join(new_L[3:6]), ''.join(new_L[6:10])
print(f"CODE = {p1}-{p2}-{p3}")

"""
LAB # 05: Implementation of Nested Loops and Function Scope in Python
"""

# %% Q#2: Completing Code

for i in range(1, 6):
    for j in range(1, i+1):
        print(i, sep='', end='')
    print()

# %% Q#3: Writing Code From Flowchart

for x in range(1, 4):
    for y in range(1, 4):
        print(f"({x}, {y}) ", end='')
    print()

# %% Q#4: Prime Factors


def primeFactors(x):
    # initialize a list to store the factors and their counts
    factors = []

    # iterate through potential factors from 2 to x - 1
    for factor in range(2, x):
        # check if factor is a divisor of x
        if x % factor == 0:
            # initialize count of the factor's occurrences
            count = 0
            # while x is divisible by the factor, keep dividing
            while x % factor == 0:
                # increase the count for each occurrence
                count += 1
                # divide x by the factor
                x //= factor

            # append the factor and its count to the list
            if count > 1:
                factors.append(f"{factor}**{count}")
            else:
                factors.append(f"{factor}")

    # print the factors in the given format
    print(', '.join(factors))


# test cases
primeFactors(70)
primeFactors(16)
primeFactors(48)
primeFactors(55)

# %% Q#5: Prime Numbers (till 50))

num = 50

# iterate through each number from 2 to num
for i in range(2, num + 1):
    # assume the current number is prime initially
    is_prime = True

    # check divisibility from 2 up to i - 1
    for j in range(2, i):
        # if i is divisible by j, it's not prime
        if i % j == 0:
            # mark as not prime
            is_prime = False
            # exit the inner loop since we found a divisor
            break

    # if the number is still marked as prime
    if is_prime:
        # print the number
        print(i, end=' ')

# %% Q#6: Printing Pyramids

rows_ = int(input("Enter no. of row of the pyramid: "))

for i in range(rows_):
    for j in range(rows_ - i - 1):
        print(' ', end='')
    for k in range(2*i + 1):
        print('*', end='')
    print()

# alternate method
# print('\n'.join(f"{'*'*(2*i+1): ^{2*rows_}}" for i in range(rows_)))

# %% Q#7: Printing Diamonds

rows = int(input("Enter no. of row of the diamond: "))

for i in range(rows//2 + 1):
    for j in range(rows//2 - i):
        print(' ', end='')
    for k in range(2*i + 1):
        print('*', end='')
    print()

for i in range(rows//2 - 1, -1, -1):
    for j in range(rows//2 - i):
        print(' ', end='')
    for k in range(2*i + 1):
        print('*', end='')
    print()

# alternate method
# print('\n'.join(f"{'*'*(2*i+1): ^{2*rows}}" for i in range(rows)))
# print('\n'.join(f"{'*'*(2*i+1): ^{2*rows}}" for i in range(rows-2, -1, -1)))

# %% Pre LAB Task (Date: 25-09-2024)

num_rows = int(input("Enter the number of rows: "))
star_count = 1

for curr_row in range(num_rows, 0, -1):
    for space in range(1, curr_row):
        print(' ', end='')

    for star in range(1, star_count+1):
        print('*', end='')

    print()
    star_count += 1

# alternate method
# print('\n'.join(f"{'*' * (curr_row + 1) : >{num_rows}}" for curr_row in range(num_rows)))

# %% LAB Task (Date: 26-09-2024)

num_rows = int(input("Enter no. of rows of the diamond: "))

# upper part (inverted equilateral triangle)
for curr_row in range(num_rows // 2, -1, -1):
    for space in range(num_rows // 2 - curr_row):
        print(' ', end='')
    for star in range(2 * curr_row + 1):
        print('*', end='')
    print()

# lower part (regular equilateral triangle)
for curr_row in range(num_rows // 2):
    for space in range(num_rows // 2 - curr_row - 1):
        print(' ', end='')
    for star in range(2 * curr_row + 3):
        print('*', end='')
    print()

# %% Q#8: Function As A Function’s Arguments


def foo(n, f, g):
    return f(g(n)) == g(f(n))


def add_one(n):
    return n+1


def square(n):
    return n*n


print(foo(4, add_one, square))
print(foo(0, add_one, square))

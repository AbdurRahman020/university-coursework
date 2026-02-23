"""
LAB # 04: Implementation of Non-Nested Loops and Strings in Python
"""

# %% Q#3: Eliminating Errors

z = int(input("enter the number of times you want to print: "))
y = 1

# in manual, no semicolon (:) is in given code
while (y <= z):
    print("Hello World")
    # old: y = y + 2, this was incrementing 'y' by 2
    y = y + 1

# %% Q#4: Printing Multiple Times Using Function


def f(name, n):
    for i in range(n):
        print(name)


# test cases
f('ali', 5)
f('Parrrot', 3)
f('yahya', 10)

# %% Q#5: Use Of Functions To Get The Desired Output


def print_even(n):
    count = 0

    for i in range(n):
        # if number is even and dvisible by 3 (same as divsion by 6)
        if i % 2 == 0 and i % 3 == 0:
            print(i)
            count += 1

    print(f"The number of integers = {count}")


# test cases
print_even(30)
print_even(50)

# %% Q#6: Completing The Code


def baz():
    print("1234567890123456")
    print("Integer   Square")

    x = 1
    while x <= 9:
        print(x, '\t\t ', x**2)
        x += 1


baz()

# %% Q#7: Prompting The User To Get The Desired Output

while True:
    num = int(input("Enter a no.: "))
    print(num)

    # if num > 5 is True, then terminate the loop
    if num >= 5:
        print("end")
        break


# %% Q#8: Iterating Over A String

def foo(x):
    # initialize the counter variables
    count_1, count_2, count_3 = 0, 0, 0

    # iterating over string's each character
    for i in x:
        # if 1 is found, incremnent the count_1
        if i == '1':
            count_1 += 1
        # if 2 is found, incremnent the count_2
        elif i == '2':
            count_2 += 1
        # if 3 is found, incremnent the count_3
        elif i == '3':
            count_3 += 1

    print(f"In {x}")
    print(f"The numbers of 1's is: {count_1}")
    print(f"The numbers of 2's is: {count_2}")
    print(f"The numbers of 3's is: {count_3}")


# test cases
foo("12313131313")
foo("1233")
foo("1111233")
foo("12213233")

# %% Question#9: Decoding A Secret Message


def getSecretMessage(s, key):
    # initialize the empty string to store decoded message
    message = ''

    # traverse the encoded string
    for i in range(len(s)):
        # if key is found
        if s[i] == key:
            # add the next word of the key to message (given pattern)
            message += s[i+1]

    # return the decoded message
    return message


# test cases
print(getSecretMessage("qcqoqmqpquqtqeqr", "q"))
print(getSecretMessage("orupqcrzypqomqmhcyqpwhhqutqtxtqeyeqrpa", "q"))

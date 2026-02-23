"""
LAB # 09: Dictionaries and Exception Handling in Python
"""

from time import time
from math import sqrt

# %% Q#1 Code 1


def ct2(d, key):
    while (key in d) and ((key+2) not in d):
        d[key+2] = key+1
        key = d[key]

    L = []
    for key in sorted(d.keys()):
        L.append(10*key + d[key])

    return L


print(ct2({1: 5, 0: 2}, 0))

# %% Q#1 Code 2

d = {1: 1, 2: 'a', 3: 0, 4: '1', 5: [1, 2], 6: {'a': 1, 'b': 3}}

for k in d:
    try:
        if k < 4:
            print(1/d[k])
            print(2)
        elif k == 3:
            print(3*n)
        elif k == 5:
            print(d[k][2])
        elif k == 6:
            print(d[k]['c'])

    except TypeError:
        print('b')
    except ZeroDivisionError:
        print('c')
    except NameError:
        print('d')
    except:
        print('e')
    else:
        print("No Excpetion")
    finally:
        print('finally')

# %% Q#2 Creating Dictionary

city_dict = {
    'Lahore': 'Punjab',
    'Peshawar': 'KPK',
    'Karachi': 'Sindh',
    'Quetta': 'Balochistan',
    'Gilgit': 'GB'
}

k = input("Enter city: ")
v = city_dict[k]
print(f"{k} is in {v}")

# %% Q#3 Mapping using Dictionary


def foo(s):
    # initialize an empty dictionary to store the frequency of each character
    freq_dict = {}

    # iterate over each character in the string
    for ch in s:
        # if the character is already in the dictionary, increment its count by 1
        if ch in freq_dict:
            freq_dict[ch] += 1
        # otherwise, add the character to the dictionary with a count of 1
        else:
            freq_dict[ch] = 1

    # return the dictionary containing the frequency of each character
    return freq_dict


print(foo('banana'))

# %% Q#4 Dictionary which returns required output


def foo(bookInfo, author):
    # iterate through each item (key-value pair) in the dictionary 'bookInfo'
    for book, book_author in bookInfo.items():
        # check if the 'book_author' matches the given 'author'
        if book_author == author:
            # if a match is found, return the book name (the key)
            return book
    # if no match is found after checking all items, return None
    return None


books_catalogue = {
    'The Hobbit': 'JRR Tolkein',
    "Harry Potter and the Sorcerer's Stone": "Jk Rowling",
    'A Game of Thrones': 'George RR Martin'
}

print(foo(books_catalogue, "Jk Rowling"))

# %% Q#5 Dictionary which returns key-value pair


def groceryCount(fruits):
    # initialize an empty dictionary to store the count of each fruit
    fruit_count_dict = {}

    # iterate over each fruit in the provided list
    for fruit in fruits:
        # check if the fruit is plural (ends with 's')
        if fruit[-1] == 's':
            # remove the last 's' to get the singular form of the fruit
            single_fruit = fruit[:-1]
            # if the singular fruit is already in the dictionary, increment its count by 3
            if single_fruit in fruit_count_dict:
                fruit_count_dict[single_fruit] += 3
            # otherwise, add the singular fruit with a count of 3
            else:
                fruit_count_dict[single_fruit] = 3
        else:
            # if the fruit is in singular form, increment its count by 1
            if fruit in fruit_count_dict:
                fruit_count_dict[fruit] += 1
            # otherwise, add the singular fruit with a count of 1
            else:
                fruit_count_dict[fruit] = 1

    # return the dictionary containing the count of each fruit
    return fruit_count_dict


print(groceryCount(['apple', 'bananas', 'kiwis', 'orange', 'kiwi', 'apple']))

# %% Q#6 Catching Exception in a code

a, b, c = 0, 1, -2

try:
    r1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    r2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    print(f"The roots are {r1} and {r2}")
except ZeroDivisionError:
    # handling the case where coefficient 'a' is zero (division by zero error)
    print("Coefficient 'a' can't be zero!")

# %% Q#7 Handling Exceptional cases in the given code

# un-comment to check a particular case

# d1 = {'ali': [10, 2, 0], 'amna': [6, 1, 8]}     # Case 1
d1 = {'ali': [1, 7], 'amna': []}               # Case 2
# d1 = {'ali': [12, 7], 'amna': [7, 'F']}         # Case 3
# d1 = {'ali': ['a', 7], 'amna': [7, 1]}          # Case 4

d2 = {}

# iterate over each key in dictionary d1
for k in d1:
    try:
        # check if the list for the current key is empty
        if len(d1[k]) == 0:
            raise ValueError(f"{k}'s list can't be empty!")

        # initialize sum (s) and index (idx) variables
        s, idx = 0, 0

        # iterate over the elements of the list for the current key
        for m in d1[k]:
            try:
                # try adding the element to the sum
                s += m
            except TypeError:
                # if an invalid element (non-numeric) is found, print an error message
                print(f"{k}'s list contains invalid input '{
                      m}' at index {idx}")
                break
            idx += 1
        # if no error occurred, store the average (sum / length of list) in d2
        else:
            d2[k] = s / len(d1[k])

    except TypeError as te:
        # handle TypeError if list elements themselves cause an issue
        print(f"{te}")
        break

    except ValueError as ve:
        # handle ValueError if list is empty
        print(f"{ve}")
        break

print(d2)

# %% Catching Exception in a Function


def CalculateRoots(a, b, c):
    # check if coefficient 'a' is a number (int or float)
    if type(a) is not int and type(a) is not float:
        raise TypeError("coefficient 'a' should be a number!")

    # check if coefficient 'b' is a number (int or float)
    if type(b) is not int and type(b) is not float:
        raise TypeError("coefficient 'b' should be a number!")

    # check if coefficient 'c' is a number (int or float)
    if type(c) is not int and type(c) is not float:
        raise TypeError("coefficient 'c' should be a number!")

    # check if coefficient 'a' is zero, as division by zero is not allowed
    if a == 0:
        raise ZeroDivisionError("coefficient 'a' can't be zero!")

    r1, r2 = (-b + sqrt(b**2 - 4*a*c)) / \
        (2*a), (-b - sqrt(b**2 - 4*a*c)) / (2*a)

    return r1, r2


# try block to catch exceptions
try:
    root1, root2 = CalculateRoots(0, 3, 3)
    print(f"the roots are {root1} and {root2}")
# catch ZeroDivisionError if 'a' is zero
except ZeroDivisionError as e:
    print(e)
# catch TypeError if any coefficient is not a number
except TypeError as e:
    print(e)

# %% Catching Exception in A Loop


def sum_integers():
    # initialize total to store the sum of integers
    total = 0

    # start an infinite loop to continuously ask for user input
    while True:
        # prompt the user to enter an integer
        user_input = input("Enter an integer: ")
        try:
            # try to convert the input to an integer
            num = int(user_input)
            # if the input is 0, break the loop to stop the summing process
            if num == 0:
                break
            # add the integer to the total sum
            total += num
        except ValueError:
            # if the input is not a valid number, print an error message
            print("Didn't enter a Number. Try again!")

    # print the total sum of entered integers when the loop ends
    print(f"The total sum of entered integers is: {total}")


sum_integers()

# %% Memoization


# Factorial function (without memoization)

def fact1(n):
    # base case: if n is 1, return 1
    if n == 1:
        return 1
    else:
        # calculate the factorial recursively
        s_p = n - 1
        s_r = fact1(s_p)
        f_r = n * s_r
        return f_r


start1 = time()

for x in range(1, 250):
    fact1(x)

end1 = time()

print(f'Execution Time = {(end1 - start1) * 1000:.4f} ms')

# ------------------------------------------------------------------------------

# initialize an empty dictionary for memoization
memo = {}

# Factorial function (with memoization)


def fact2(n):
    # if the result is already in the memo dictionary, return it
    if n in memo:
        return memo[n]
    elif n == 1:
        return 1
    # otherwise, calculate the factorial recursively
    else:
        s_p = n - 1
        s_r = fact2(s_p)
        # store the computed value in the memo dictionary
        memo[n] = n * s_r
        return memo[n]


start2 = time()

for x in range(1, 250):
    fact2(x)

end2 = time()

print(f'Execution time with memoization = {(end2 - start2) * 1000:.4f} ms')

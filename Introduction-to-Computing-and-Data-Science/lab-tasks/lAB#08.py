"""
LAB # 08: Implementation of Recursion in Python
"""

from ucb import trace

# Short Forms Used:
#   s_p = smaller problem
#   s_r = smaller result
#   f_r = final result
#   L = Left
#   R = Right

# %% Q#1 Code 1


def bonusCt1(n):
    def f(x):
        return x and (2*x) - 1 + f(x-1)

    def g(x):
        return x and 1+g(x//2)

    while f(g(n)) != n:
        n = f(g(n))

    return n


print(bonusCt1(31))

# %% Q#1 Code 2 The Mutual Recurrsion - The LUHN Algorithm


def sum_digits(n):
    # base case: if the number is less than 10, return the number itself
    if n < 10:
        return n
    else:
        # split the number into all but the last digit and the last digit
        all_but_last, last = n // 10, n % 10
        # recursively sum the digits of the remaining number and add the last digit
        return sum_digits(all_but_last) + last


def luhn_sum(n):
    # base case: if the number is less than 10, return the number itself
    if n < 10:
        return n
    else:
        # split the number into all but the last digit and the last digit
        all_but_last, last = n // 10, n % 10
        # recursively calculate the Luhn sum of the remaining number, then add the last digit
        return luhn_sum_double(all_but_last) + last


def luhn_sum_double(n):
    # split the number into all but the last digit and the last digit
    all_but_last, last = n // 10, n % 10
    # double the last digit and calculate the sum of its digits (if greater than 9)
    luhn_digit = sum_digits(2 * last)

    # base case: if the number is less than 10, return the doubled last digit
    if n < 10:
        return luhn_digit
    else:
        # recursively apply the Luhn sum for the remaining number, adding the processed last digit
        return luhn_sum(all_but_last) + luhn_digit


print(luhn_sum(6649))

# %% Q#2: Errors (Decimal Number To Binary Number)


def foo(n):
    # base case: if n is 1, return the string "1"
    if n == 1:
        return str(1)
    else:
        # recursive case: concatenate remainder of n divided by 2 with result of foo(n//2)
        return str(n % 2) + foo(n//2)


print(foo(55))
print(foo(127))
print(foo(4294967295))  # 2^32 - 1
print(foo(9223372036854775807))  # 2^63 - 1
print(foo(18446744073709551615))  # 2^64 - 1

# %% Q#3 Writing A Recursive Function


@trace
def mul(m, n, depth=0):
    # increase the depth for current recursion level
    depth += 1

    # base case: if n is 0, the product is 0
    if n == 0:
        f_r = 0
    else:
        # smaller problem: subtract 1 from n
        s_p = n - 1
        # recursively calculate product for smaller problem
        s_r = mul(m, s_p, depth)
        # final result: add m to result of smaller problem
        f_r = m + s_r

    # print the current depth and the result of mul(m, n)
    print(f"depth {depth}: mul({m}, {n}) = {f_r}")

    # return the final result
    return f_r


print(f"\nproduct is: {mul(-5, 7)}")
print(f"\nproduct is: {mul(13, 7)}")

# %% Q#4: Recursive Function Which Returns Sum Of Numbers

# Part: A


def add1(L):
    # base case: if an empty list, then return 0
    if len(L) == 0:
        return 0
    else:
        # smaller problem: list excluding the first element
        s_p = L[1:]
        # recursively solve smaller problem and store the result
        s_r = add1(s_p)
        # final result is first element of the list plus the result of the smaller problem
        f_r = L[0] + s_r
        # return the final result (sum of all elements in the list)
        return f_r


print(add1([1, -2, 3, -4, 5]))
print(add1([5, 6, -7, -17, 9, 3/2]))

# ------------------------------------------------------------------------------

# Part: B Tree Recurrsion


def add2(L):
    # base case 1: if list is empty, return 0 (sum of an empty list is 0)
    if len(L) == 0:
        return 0
    # base case 2: if list has only one element, return that element
    elif len(L) == 1:
        return L[0]
    else:
        # smaller problem: divide the list into two halves: left half (s_p_L) and
        # right half (s_p_R)
        s_p_L = L[:len(L)//2]
        s_p_R = L[len(L)//2:]
        # recursively solve for the left half (s_r_L) and right half (s_r_R)
        s_r_L = add2(s_p_L)
        s_r_R = add2(s_p_R)
        # final result is sum of the results of the left and right halves
        f_r = s_r_L + s_r_R
        # return final result (sum of all elements in list)
        return f_r


print(add2([1, -2, 3, -4, 5]))
print(add2([5, 6, -7, -17, 9, 3/2]))

# %% Q#5: Recursive Function Which Returns Number Of Vowels In A String


def NoOfVowels(s):
    # base case: if empty string, return 0
    if len(s) == 0:
        return 0
    else:
        # smaller problem: string excluding the first character
        s_p = s[1:]
        # recursively solve smaller problem and store the result
        s_r = NoOfVowels(s_p)

        # check if the first character is a vowel
        if s[0] in 'AEIOUaeiou':
            # final result if the first character is a vowel
            # add 1 to the smaller result
            f_r = 1 + s_r
            # return the final result, with increment
            return f_r
        else:
            # final result if the first character is not a vowel
            f_r = s_r
            # return final result i.e. without increment
            return f_r


print(NoOfVowels("aeiou"))
print(NoOfVowels("The quick brown fox jumps over the lazy dog"))

# %% Q#6: Complete The Code


def RemoveDuplicates(L):
    if len(L) == 1:
        return L
    else:
        sp = L[1:]
        sr = RemoveDuplicates(sp)
        if L[0] not in sr:
            r = [L[0]] + sr
        else:
            r = sr
        return r


print(RemoveDuplicates([1, 2, 1, 2, 3, 4, 3, 3]))

# %% Q#7: Recursive Function Which Returns Number Of Indices


def RecursiveMatch(L1, L2):
    # base case: if either list is empty, return 0
    if len(L1) == 0 or len(L2) == 0:
        return 0
    else:
        # smaller problem: lists excluding the first elements
        s_p_1, s_p_2 = L1[1:], L2[1:]
        # recursively solve smaller problem and store the result
        s_r = RecursiveMatch(s_p_1, s_p_2)
        # check if the first elements of both lists match

        if L1[0] == L2[0]:
            # final result if they match
            f_r = 1 + s_r
            # add 1 to the smaller result
            return f_r
        else:
            # final result if they don't match
            f_r = s_r
            # just return that smaller result without increment
            return f_r


print(RecursiveMatch([4, 1, 2, 3], [4, 6, 7, 3]))

# %% Q#8: Recursive Function Which Returns Longest String In A List


def recursiveLongestString(L):
    # base case: if there's only one string in the list, return it
    if len(L) == 1:
        return L[0]
    else:
        # smaller problem: list excluding the first element
        s_p = L[1:]
        # recursively solve smaller problem and store the result
        s_r = recursiveLongestString(s_p)

        # check if the first string is longer than the result from the smaller problem
        if len(L[0]) > len(s_r):
            # final result: if the first string is longer
            f_r = L[0]
            # return the first string
            return f_r
        else:
            # final result: if the smaller result is longer or equal
            f_r = s_r
            # return that smaller result
            return f_r


print(recursiveLongestString(["a", "bb", "ccc"]))
print(recursiveLongestString(["hi", "its", "fantastic", "here"]))

# %% Q#9: Recursive Hailstone


def hailStone(n, steps=0):
    # base case: if n is 1, print 'n' and return number of steps
    if n == 1:
        print(n, end=' ')
        return steps

    # print the current value of 'n
    print(n, end=' ')

    # smaller problems: check if n is even or odd
    if n % 2 == 0:
        # even 'n': halve 'n' and increase step count
        s_p = n // 2
        # recursive call
        s_r = hailStone(s_p, steps + 1)
        # final result (steps) is returned after recursive call
        f_r = s_r
        # return number of steps from recursive call
        return f_r
    else:
        # odd 'n': apply the 3n+1 rule and increase step count
        s_p = 3 * n + 1
        # recursive call
        s_r = hailStone(s_p, steps + 1)
        # final result (steps) is returned after recursive call
        f_r = s_r
        # return number of steps from recursive call
        return f_r


print(f"\nTotal steps: {hailStone(10)}")
print(f"\nTotal steps: {hailStone(45)}")

# %% Q#10: Recursive Merge


def merge(L1, L2):
    # base case: if L2 is empty, return L1 as the result
    if not L2:
        return L1
    # base case: if L1 is empty, return L2 as the result
    if not L1:
        return L2

    # if first element of L1 is smaller than the first element of L2
    if L1[0] < L2[0]:
        # smaller problem: list (L1) excluding first element
        s_p_L1 = L1[1:]
        # recursively merge smaller problem (rest of L1 and whole L2)
        s_r_L1 = merge(s_p_L1, L2)
        # final result is first element of L1 combined with result of recursive merge
        f_r_L1 = [L1[0]] + s_r_L1
        # return merged result for case where first element of L1 is smaller than
        # first element of L2
        return f_r_L1
    # if first element of L2 is smaller than or equal to first element of L1
    else:
        # smaller problem: list (L2) excluding first element
        s_p_L2 = L2[1:]
        # recursively merge smaller problem (whole L1 and rest of L2)
        s_r_L2 = merge(L1, s_p_L2)
        # final result is first element of L2 combined with result of recursive merge
        f_r_L2 = [L1[0]] + s_r_L2
        # return merged result for case where first element of L2 is smaller than
        # first element of L1
        return f_r_L2


print(merge([2, 3, 5, 7, 9], [0, 1, 4, 6, 8]))
print(merge([2, 3, 4], [2, 4, 6]))
print(merge([], [2, 3, 4]))
print(merge([1, 2, 3, 4,], []))

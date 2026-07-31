'''
lECTURES aND lABS

Source:
    Ana Bell - Get Programming: Learn To Code With Python (2018)
Note:
    Approximately 70% of the code is adapted or modified from the above book.
'''
# from IPython import get_ipython
# get_ipython().run_line_magic('reset', '-sf')

# %% Recurrsion: Power of a Number


def power_recur(n, p):
    # base case: if power 'p' is 0, return 1
    if p == 0:
        return 1
    # base case: if power 'p' is 1, return number 'n'
    elif p == 1:
        return n
    else:
        # samller problem: one minus the total power
        s_p = p - 1
        # rsecursively solve the smaller problem and store the result
        s_r = power_recur(n, s_p)
        # final result: multiple the number with result of smaller problem
        f_r = n * s_r
        # return the final result
        return f_r


print(power_recur(10, 6))

# %% Recurrsion: Printing Elements of a list

# element by element


def printList01(L):
    if not L:
        return
    else:
        print(L[0], end=' ')
        printList01(L[1:])


printList01([1, 5, 4, 2, 3])

print()

# %% Total number of elements in a list which contain strings


def total_len_recur(L):
    # base case: if L is empty, return 0
    if len(L) == 0:
        return 0
    else:
        # smaller problem: the rest of the list excluding the first element
        s_p = L[1:]
        # rsecursively solve the smaller problem and store the result
        s_r = total_len_recur(s_p)
        # final result: add the length of the first element to the result of
        # the smaller problem
        f_r = len(L[0]) + s_r
        # return the final result
        return f_r


print(total_len_recur(['ab', 'c', 'defgh']))

# %% Recurrsion: Searching an element in 1D list


def in_list(L, e):
    # base case: if L is empty, return False
    if len(L) == 0:
        return False
    else:
        # smaller problem: the rest of the list excluding the first element
        s_p = L[1:]
        # recursively solve the smaller problem and store the result
        s_r = in_list(s_p, e)
        # final result: if the first element is equal to e, return True
        if L[0] == e:
            f_r = True
        # otherwise return the result from the recursive call
        else:
            f_r = s_r
        # return the final result
        return f_r


print(in_list([2, 5, 8, 1], 8))

# %% Recurrsion: Searching an element in a 2D list


def in_list_of_lists(L, e):
    # base case: if L is empty, return False
    if len(L) == 0:
        return False
    else:
        # smaller problem: sublist excluding the first list
        s_p = L[1:]
        # recursively solve smaller problem and store the result
        s_r = in_list_of_lists(s_p, e)
        # check if e is in the first sublist of L
        if e in L[0]:
            # final result if e is in the first sublist
            f_r = True
            # return the final result
            return f_r
        else:
            # final result if e is not in the first sublist
            f_r = s_r
            # return final result
            return f_r


print(in_list_of_lists([[1, 2], [3, 4, 5], [8, 7, 6]], 4))

# %% Recurrsion: Mod


def in_list_of_lists_mod(L, e):
    if len(L) == 1 and type(L[0]) is not list:
        # base case: one element, not a list
        return e == L[0]
    elif len(L) == 1 and type(L[0]) is list:
        # base case: one element, which is a list
        return e in L[0]
    else:
        # recursive case: first element is not a list
        if type(L[0]) is not list:
            # smaller problem, the rest of the list
            s_p = L[1:]
            # recursive call for the rest
            s_r = in_list_of_lists_mod(s_p, e)
            # final result is whether first element equals 'e' or 'e' is found
            # in the rest
            f_r = e == L[0] or s_r
            # return the final result
            return f_r
        # first element is a list
        elif type(L[0]) is list:
            # smaller problem, the rest of the list
            s_p = L[1:]
            # recursive call for the rest
            s_r = in_list_of_lists_mod(s_p, e)
            # final result is whether 'e' is in the first list or in the rest
            f_r = e in L[0] or s_r
            # return the final result
            return f_r


print(in_list_of_lists_mod([[1, 2], 3, 4, 5, 6, 7], 3))
print(in_list_of_lists_mod([[1, 2], [3, 4, 5], 6, 7], 9))

# %% Recurrsion: 2D list flattening


def flatten(L):
    # base case: if L is empty, return an empty list
    if len(L) == 0:
        return []
    else:
        # smaller problem: flatten the rest of the list (excluding the
        # first element)
        s_p = L[1:]
        # recursively solve the smaller problem and store the result
        s_r = flatten(s_p)
        # final result: concatenate the first sublist with the flattened rest
        # of the list
        f_r = L[0] + s_r
        # return the final result
        return f_r


print(flatten([[1, 2], [3, 4, 5], [8, 7, 6]]))

# %%


def my_rev(L):
    # base case: if L is empty or has only one element, return L
    if len(L) == 0:
        return L
    else:
        # smaller problem: the rest of the list excluding the first element
        s_p = L[1:]
        # recursively solve the smaller problem and store the result
        s_r = my_rev(s_p)
        # final result: concatenate the reversed rest of the list with
        # the first element
        f_r = s_r + [L[0]]
        # return the final result
        return f_r


print(my_rev([1, 2, 'abc']))
print(my_rev([1, ['d'], ['e', ['f', 'g']]]))

# %%


def deep_rev(L):
    # base case: if L is empty, return an empty list
    if L == []:
        return []
    else:
        # smaller problem: the rest of the list excluding the first element
        s_p = L[1:]
        # recursively solve the smaller problem and store the result
        s_r = deep_rev(s_p)
        # final result: if the first element is not a list, reverse it and add
        # it to the result
        if type(L[0]) is not list:
            f_r = s_r + [L[0]]
        else:
            # if the first element is a list, reverse it deeply
            f_r = s_r + [deep_rev(L[0])]
        # return the final result
        return f_r


print(deep_rev([[1, 2], [3, 4, 5], [8, 7, 6]]))

# %% Recurrsion: No. of repeation of an element in a list


def no_of_rep_in_L(L, e):
    # base case: if the list is empty, return 0
    if len(L) == 0:
        return 0
    else:
        # smaller problem: list excluding the first element
        s_p = L[1:]
        # recursively solve the smaller problem and store the result
        s_r = no_of_rep_in_L(s_p, e)
        # check if the first element is equal to 'e'
        if L[0] == e:
            # final result if the first element matches 'e' add 1 to the
            # smaller result
            f_r = 1 + s_r
        else:
            # final result if the first element does not match 'e'
            f_r = s_r
        # return the final result
        return f_r


print(no_of_rep_in_L([1, 2, 3, 1], 1))
print(no_of_rep_in_L([1, 2, 1, 1, 3, 1], 1))

# %% Recurrsion: No. of repeation of an element in nested list


def no_of_rep_in_list_of_lists(L, e):
    # base case: if the list is empty, return 0
    if len(L) == 0:
        return 0
    else:
        # smaller problem: list excluding the first element
        s_p = L[1:]
        # recursively solve the smaller problem and store the result
        s_r = no_of_rep_in_list_of_lists(s_p, e)
        # check if the first element is an integer
        if type(L[0]) is int:
            # final result if the first element matches e
            if L[0] == e:
                # add 1 if a match is found
                f_r = 1 + s_r
            # no match, return the smaller result
            else:
                f_r = s_r
        # check if the first element is a list
        elif type(L[0]) is not list:
            # final result when the first element is a list, recurse on the list
            f_r = s_r + no_of_rep_in_list_of_lists(L[0], e)
        # return the final result
        return f_r


print(no_of_rep_in_list_of_lists([1, 2, [3, 1, [1, [1]]]], 1))

# %% Deep Copy of a List via Recurrsion


def my_deepcopy(L):
    # base case: if the list is empty, return an empty list
    if len(L) == 0:
        return []
    # recursive case
    else:
        # smaller problem: rest of the list
        s_p = L[1:]
        # if the first element is not a list
        if type(L[0]) is not list:
            # recursively solve for the rest
            s_r = my_deepcopy(s_p)
            # combine the first element with the result of the rest
            f_r = [L[0]] + s_r
        # if the first element is a list
        else:
            # recursively solve for the rest
            s_r = my_deepcopy(s_p)
            # deepcopy the first sublist and combine
            f_r = [my_deepcopy(L[0])] + s_r
        # return the final result
        return f_r


myL = ["abc", ['d'], ['e', ['f', 'g']]]
my_newL = my_deepcopy(myL)

print(f"Original list: {myL}")
print(f"Deep copy of the list: {my_newL}")

myL[2][1][0] = 1
print(f"Modified original list: {myL}")
print(f"Deep copy should remain unchanged: {my_newL}")

# %% Tower of Hanoi (1)


def print_move(fr, to):
    print(f"move from {fr} to {to}")


def towers(n, fr, to, spare):
    if n == 1:
        print_move(fr, to)
    else:
        towers(n-1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n-1, spare, to, fr)


towers(3, 'a', 'b', 'c')

# %% Tower of Hanoi (2)

step_counter = 0


def move_disk_print(fr, to, disk):
    global step_counter
    step_counter += 1
    print(f"move disk {disk} from {fr} to {to}")


def towerOfHanoi(n, src, dest, aux):
    global step_counter
    # base case: if only one disk is left, just move it
    if n == 1:
        move_disk_print(src, dest, 1)
    else:
        # smaller problem: move n-1 disks from src to aux using dest as auxiliary
        towerOfHanoi(n - 1, src, aux, dest)
        # move the nth disk from src to dest
        move_disk_print(src, dest, n)
        # solve the smaller problem: move n-1 disks from aux to dest using
        # src as auxiliary
        towerOfHanoi(n - 1, aux, dest, src)

    return step_counter


no_of_disks = 3
towerOfHanoi(no_of_disks, 'peg 1', 'peg 2', 'peg 3')

print(f"\nnumber of steps for {no_of_disks} disks: {step_counter}")
print(f"number of steps can be calculated as 2^{
      no_of_disks} - 1: {2**no_of_disks - 1}")

# %% Recurrsion & Memoization: Fibonacci Numbers

# initialize the dictionary with base cases for fibonacci
d = {1: 1, 2: 1}


def fib(n, d):
    try:
        # base case: if n is negative, raise an exception
        if n < 0:
            raise ValueError("Provide positive value for index")
        # if the value of n is already computed, return it from the dictionary
        elif n in d:
            return d[n]
        else:
            # smaller problems: compute the two preceding fibonacci numbers
            s_p_1 = n - 1
            s_p_2 = n - 2
            # recursively solve for the two smaller fibonacci numbers
            s_r_1 = fib(s_p_1, d)
            s_r_2 = fib(s_p_2, d)
            # final result: add the results of the two smaller fibonacci numbers
            f_r = s_r_1 + s_r_2
            # store the result in the dictionary to avoid redundant calculations
            d[n] = f_r
            # return the final result
            return f_r
    except ValueError as ve:
        print(ve)


print(fib(-1, d))
print(fib(6, d))
print(fib(4, d))

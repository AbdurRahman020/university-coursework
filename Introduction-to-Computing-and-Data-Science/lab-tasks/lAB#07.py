"""
LAB # 07: Implementation of 1D and 2D Lists in Python
"""

from random import randint
import copy

# %% Q#1 Code 1


def foo(a):
    for i in range(len(a) - 1, -1, -1):
        if (a[i] == 3):
            a.pop(i)


L = [2, 3, 5, 3, 7]
foo(L)
print(L)

# %% Q#1 Code 2


def foo(a):
    for item in a:
        if (item == 3):
            a.remove(item)


L = [3, 3, 2, 3, 7]
foo(L)
print(L)

# %% Q#1 Code 3


def chain(s):
    return [s[0], s[1:]]


silver = [2, chain([3, 4, 5])]
gold = [silver[0], silver[1].pop()]
silver[0] = 1
platinum = chain(chain([6, 7, 8]))

print(platinum)

# %% Q#1 Code 4


def bounsCt1(L):
    return sum([int(d) for d in str([str(c*2)*2 for c in L*2]) if d.isdigit()])


print(bounsCt1([4, 5, 6]))

# %% Q#1 Code 5


def ct1(x, r):
    y = x
    z = x[:]
    x.append(10)
    y[0] += 3
    x = x[2:]
    print(f"x = {x}")
    x[-1] = x[1] + x[0]
    z.pop(0)

    w = r
    s = copy.deepcopy(w)
    w.append([5, 6, 7])
    r[0].append(5)
    s[2][1] = 'a'

    return (x[-1], y[-1], z[-1], w[2], s)


L = [47, 80, 112]
A = [[x+1]*x for x in range(3)]

print(f"ct = {ct1(L, A)}")
print(f"L = {L}")
print(f"A = {A}")

# %% LAB Task (Random Elements List)


random_ele_list = []

num_of_ele = 50

start_index, end_index = 100, 150

for i in range(num_of_ele):
    random_ele_list.append(randint(start_index, end_index))

print('random elements list: ', random_ele_list)

# %% Q#2: 1D List

list_sum, count, avg = 0, 0, 0

price = [40, 5.3, 7.8, 1]

for i in range(len(price)):
    list_sum += price[i]
    count += 1
    print(f"{i} {price[i]}")

if count > 0:
    avg = list_sum / count
    print(f"The sum is {list_sum} and average price is {avg}")
else:
    print("empty list, thus no average")

# list_sum, count, avg = sum(price), len(price), sum(price) / len(price) if price else 0
# print(f"The sum is {list_sum} and average price is {avg}" if count > 0 else "empty list, thus no average")

# %% Q#3: Insert Elements Into List

num_of_items = 10
L = []

if num_of_items > 0:
    for i in range(num_of_items + 1):
        L.append(i)
else:
    print("Number of elements in a list can't be negative!")

print(L)

# %% Q#4: Squaring The Original List

L = [1, 2, 3, 4, 5]
print(f"before squaring L: {L}")

for i in range(len(L)):
    # in place squarng of elements
    L[i] **= 2

print(f"after squaring L: {L}")

# %% Q#5: Squaring But Making A New List To Store Elements

L = [1, 2, 3, 4, 5]
print(f"before squaring L: {L}")
# make a new list
L_new = []

for i in range(len(L)):
    # append squared elements to new list
    L_new.append(L[i]**2)

print(f"after squaring L_new: {L_new}")

# %% Q#6: Transfer Even Integers From An Old List To A New List

L_old = [1, 2, 3, 4, 5, 6]
print(f"L_old: {L_old}")

L_new = []

# iterate over each element of given list
for i in range(len(L_old)):
    # if even number is found
    if L_old[i] % 2 == 0:
        # append it to new list
        L_new.append(L_old[i])

print(f"L_new: {L_new}")

# %% Question#7: Insert Square Elements In A List Via Function


def f(L):
    # iterate over each element of L
    for i in range(len(L)):
        # in place squaring of elements
        L[i] **= 2


L = [1, 2, 3, 4, 5]
print('before squaring L =', L)
f(L)
print('after squaring L =', L)

# %% Q#8: A Function That Returns A New List Of Squared Elements


def f(L):
    # make a new list
    list_new = []
    # iterate over each element of L
    for i in range(len(L)):
        # add items into new list
        list_new.append(L[i]**2)

    return list_new


L = [1, 2, 3, 4, 5]
print('before squaring L =', L)
L_new = f(L)
print('after squaring L =', L_new)

# %% Q#9: Accessing 2D List Elements Via Indexing

L = [[1, 2], [3, 4], [5, 6]]

# iterate over each row of 2D list
for r in range(len(L)):
    # iterate over each column of 2D list
    for c in range(len(L[0])):
        # print each element
        print(L[r][c])

# one liner
# x = [[print(L[r][c]) for r in range(len(L))] for c in range(len(L[0]))]

# %% Q#10: Directly Accessing 2D List Elements

L = [[1, 2], [3, 4], [5, 6]]

# inteate over each sub list
for sub_L in L:
    # iterate over each element of sub list
    for item in sub_L:
        # print the elements in sub list
        print(item)

# one liner
# x = [[print(ele) for sub_L in L] for ele in sub_L]

# %% Q#11: In-place Squaring Of Elements In 2D List

L = [[1, 2], [3, 4], [6, 7]]
print('before squaring L =', L)

# iterate over each row of 2D list
for r in range(len(L)):
    # iterate over each column of 2D list
    for c in range(len(L[0])):
        # in place square of elements
        L[r][c] **= 2

print('after squaring L =', L)

# %% Q#12: Squaring Of Elements In A 2D List

L = [[1, 2], [3, 4], [6, 7]]
print('before squaring L =', L)

# make an empty list L_sub & L_new
L_new = []

# iterate over each row of 2D list
for r in range(len(L)):
    # make an new sub list for every iteration
    L_sub = []
    # iterate over each column of 2D list
    for c in range(len(L[0])):
        # add the elemment to L_sub
        L_sub.append(L[r][c]**2)

    # add the L_sub to L_new
    L_new.append(L_sub)

print('after squaring L_new =', L_new)

# -----------------------------------------------------------------------------

L_ = [[1, 2], [3, 4], [6, 7]]
print('before squaring L =', L)

# make an new empty list
L_new_ = []

# iterate over each row of 2D list
for sub_list in L_:
    # make an new sub list for every iteration
    L_sub_ = []
    # iterate over each column of 2D list
    for item in sub_list:
        # add the elemment to L_sub
        L_sub_.append(item)

    # add the L_sub to L_new
    L_new_.append(L_sub)

print('after squaring L_new =', L_new)

# %% Q#13: 2D List

# method 1 (without indexing)


def getProvince(city_list, city_name):
    for city, province in city_list:
        if city == city_name:
            return province

    return None


Cities_List = [["Lahore", "Punjab"], ['Gilgit', 'GB'], ["Karachi", "Sindh"]]

print(getProvince(Cities_List, "Lahore"))
print(getProvince(Cities_List, "uet"))

# method 2 (with indexing)


def getProvince(city_list, city_name):
    for city in city_list:
        if city[0] == city_name:
            return city[1]

    return None


Cities_List = [["Lahore", "Punjab"], ['Gilgit', 'GB'], ["Karachi", "Sindh"]]

print(getProvince(Cities_List, "Lahore"))
print(getProvince(Cities_List, "uet"))

print(getProvince.__type_params__)

# method 3 (one liner without indexing)
# return next((province for city, province in cityList if city == city_name), None)

# method 4 (one liner with indexing)
# return next((city[1] for city in city_list if city[0] == city_name), None)

# %% Q#14: Function Arguments as 1D Lists and 2D List Return Value + List Comprehension


def couple(a, b):
    return [[a[i], b[i]] for i in range(len(b)) if len(a) >= len(b)]


print(couple([1, 2, 3], [4, 5, 6]))

# %% Q#15: Non-Destructive Function with 1D list argument and 1D list Return Value


def findMultiple(L, num):
    list_new = []

    for i in range(len(L)):
        if L[i] % num == 0:
            list_new.append(L[i])

    return list_new


print(findMultiple([11, 20, 35, 43, 50], 5))

# %% Q#16: Destructive Function

# Part A (1D List):


def foo1D(L):
    for i in range(len(L)):
        if L[i] > 0:
            L[i] *= 2


a = [-1, 2, 3, -4]
print(a)

foo1D(a)
print(a)

# -----------------------------------------------------------------------------
# Part B (2D List):


def foo2D(L):
    for sub_L in L:
        for i in range(len(sub_L)):
            if sub_L[i] > 0:
                sub_L[i] *= 2


a = [[-1, 2], [-3, 4, 5]]
print(a)

foo2D(a)
print(a)

# for sub_L in L: [sub_L[i] * 2 for i in range(len(sub_L)) if sub_L[i] > 0]
# for sub_L in L: [sub_L.__setitem__(i, x * 2) for i, x in enumerate(sub_L) if x > 0]

# %% Q#17: Returning List From Script


def getCharacterLines(script, character):
    lines = script.split('\n')

    speeches = []
    for line in lines:
        if line[:len(character) + 1] == character + ':':
            dialogue = line.split(':', 1)[1].strip()
            speeches.append(dialogue)

    return speeches


script = '''Burr: Can I buy you a drink?
Hamilton: That would be nice.
Burr: While we're talking, let me offer you some free advice: talk less.
Hamilton: What?
Burr: Smile more.
Hamilton: Ha.
Burr: Don't let them know what you're against or what you're for.
Hamilton: You can't be serious.
Burr: You want to get ahead?
Hamilton: Yes.
Burr: Fools who run their mouths oft wind up dead.'''

print(getCharacterLines(script, 'Hamilton'))
print(getCharacterLines(script, 'Burr'))

# %% Q#18: Modifying The Code (Using while-loop)


def foo(a):
    item = 3
    while item in a:
        a.remove(item)

    print(a)


L = [3, 3, 2, 3, 7]
foo(L)

# %% Q#19: Optimizing The Code For Fast Cache Access (Non-Optimized Version)


def creatMatrix(n, value):
    # create an n x n matrix filled with the specified value
    return [[value for r in range(n)] for c in range(n)]


def rowSum(matrix):
    # initialize total sum of all rows
    total_sum = 0
    # iterate over each row in the matrix
    for r in range(len(matrix)):
        # initialize sum for the current row
        curr_row_sum = 0
        # iterate over each column in the current row
        for c in range(len(matrix[r])):
            # add the current element to the row sum
            curr_row_sum += matrix[r][c]

        # add the curr row sum to the total sum
        total_sum += curr_row_sum

    # return the total sum of all rows
    return total_sum


def columnSum(matrix):
    # initialize total sum of all rows
    total_sum = 0
    # iterate over each column in the matrix
    for c in range(len(matrix[0])):
        # initialize sum for the current column
        curr_col_sum = 0
        # iterate over each row in the current column
        for r in range(len(matrix)):
            # add the current element to the column sum
            curr_col_sum += matrix[r][c]

        # add the curr column sum to the total sum
        total_sum += curr_col_sum

    # return the total sum of all columns
    return total_sum


m = creatMatrix(3, 4)
print(f"The matrix is: {m}")
print(f"Row sum of the matrix is: {rowSum(m)}")
print(f"Column sum of the matrix is: {columnSum(m)}")

# %% Q#19: Optimizing The Code For Fast Cache Access (Optimized Version (Pythonic Version))


def createMatrix_(n, value):
    # create an n x n matrix filled with the specified value
    return [[value] * n for c in range(n)]


def rowSum_(matrix):
    # initialize total sum of all rows
    total_sum = 0
    # iterate over each row in the matrix
    for r in matrix:
        # sum each row directly since all elements are the same
        total_sum += sum(r)

    # return the total sum of all rows
    return total_sum


def columnSum_(matrix):
    # initialize total sum of all columns
    total_sum = 0
    # number of rows
    n = len(matrix)
    # iterate over each column index
    for c in range(len(matrix[0])):
        # sum each column directly since all elements are the same
        total_sum += matrix[0][c] * n

    # return the total sum of all columns
    return total_sum


m = createMatrix_(3, 4)
print(f"The matrix is: {m}")
print(f"Row sum of the matrix is: {rowSum_(m)}")
print(f"Column sum of the matrix is: {columnSum_(m)}")

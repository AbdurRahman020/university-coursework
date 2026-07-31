"""
LAB EXAM #02
DATE: 27-DEC-2024
"""

from IPython import get_ipython

# %% Q#1 Circumference of a cirlce of any radius

get_ipython().run_line_magic('reset', '-sf')

from math import pi

r = 4
print(f"For radious of {r} units, the circumference is {2 * pi * r} units.")

# %% Q#2 Dictionary elements at odd index

get_ipython().run_line_magic('reset', '-sf')

d = {
    'ana': 301,
    'bell': 124,
    'cat': 132,
    'pol': 509
}

for i, k in enumerate(d):
    if i % 2 != 0:
        print(k, d[k])

# %% Q#3 List modification

get_ipython().run_line_magic('reset', '-sf')


def fun(list1, list2):
    list_new = []
    for i in range(len(l1)):
        list_new.append(list1[i] + list2[i])

    return list_new


l1 = [10, 20, 36]
l2 = [5, 4, 6]

print(fun(l1, l2))

# %% Q#4 List with exception handling

get_ipython().run_line_magic('reset', '-sf')


def fun(list1, list2):
    list_new = []

    for i in range(len(l1)):
        try:
            list_new.append(list1[i] + list2[i])
        except:
            print("Something is fishy.")

    return list_new


l1 = [10, 20, 36]
l2 = [5, 4, 6, 8]

assert (len(l1) == len(l2))

print(fun(l1, l2))

# %% Q#5 Employee & Manager Class (Inheritance)

get_ipython().run_line_magic('reset', '-sf')


class Employee:

    def __init__(self, n, s):
        self.name = n
        self.salary = s

    def baz(self):
        return f"The salary of {self.name} is {self.salary}"

    def __str__(self):
        return f"{self.name, self.salary}"


class Manager(Employee):

    def __init__(self, n, s, jd):
        super().__init__(n, s)
        self.job_description = jd

    def __mul__(self, other):
        return Employee(other.name + self.name, self.salary * other.salary)


e1 = Employee('Head', 5)
e2 = Manager('kohli', 3, 'manage affairs')
e3 = e2 * e1

print(e1.baz())
print(e1)
print(e2.baz())
print(e2.job_description)
print(e3)

# %% Q#6 Node Class

get_ipython().run_line_magic('reset', '-sf')


class Node:

    def __init__(self, i):
        self.item = i
        self.nxt = None

    def insert(self, d):
        curr = self
        while curr.nxt is not None:
            curr = curr.nxt
        curr.nxt = Node(d)

    def insertAtIndex(self, n_itm, idx):
        curr = self

        if idx == 0:
            n = Node(n_itm)
            n.nxt = curr
            self.item = n.item
            self.nxt = n.nxt
            return

        for _ in range(idx - 1):
            if curr.nxt is None:
                return
            curr = curr.nxt

        n = Node(n_itm)
        n.nxt = curr.nxt
        curr.nxt = n

    def to_list(self):
        result = []
        curr = self
        while curr:
            result.append(curr.item)
            curr = curr.nxt
        return result


t = Node(0)

for i in range(1, 4):
    t.insert(i)

print(t.to_list())

t.insertAtIndex('new', 2)
print(t.to_list())

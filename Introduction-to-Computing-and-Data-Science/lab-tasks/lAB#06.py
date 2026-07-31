"""
LAB # 06: Implementation of Higher Order Functions in Python
"""

# %% Q#4: Function Calling A Function; Function As A Function’s Argument


def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total += term(k)
        k += 1
    return total


def sum_naturals(n):
    return summation(n, lambda num: num)


def sum_cubes(n):
    return summation(n, lambda num: num**3)


print(sum_naturals(3))
print(sum_cubes(3))

# %% Q#5: Higher Order Function Returning A Function


def multiply_by(m):
    def multiply(n):
        return m * n
    return multiply


times_three = multiply_by(3)
print(times_three(5))
print(multiply_by(3)(10))

# %% Q#6: Higher Order Function


def make_keeper(n):
    def f(cond):
        for i in range(1, n+1):
            if cond(i):
                print(i, end=' ')
        print()
    return f


def is_even(num): return num % 2 == 0
def is_odd(num): return num % 2 != 0


make_keeper(6)(is_even)
make_keeper(9)(is_odd)

# %% Q#7: Composite Functions


def compose(f, g):
    def foo(x):
        return f(g(x))
    return foo


def square(num): return num ** 2
def triple(num): return num * 3


squiple = compose(square, triple)
print(squiple(2))

tripare = compose(triple, square)
print(tripare(2))

# def compose(f, g): return lambda x: f(g(x))

# %% Q#8: Composite Functions


def compose(f, g):
    def hasBeenComposed(x):
        return f(g(x))
    return hasBeenComposed


def composite_identity(f, g):
    def identity(x):
        return compose(f, g)(x) == compose(g, f)(x)
    return identity


def add_one(num): return num + 1
def square(num): return num ** 2


foo = composite_identity(add_one, square)

print(foo(0))
print(foo(4))

# def compose_(f, g): return lambda x: f(g(x))
# def composite_identity_(f, g): return lambda x: compose_(f, g)(x) == compose_(g, f)(x)

# %% Q#9: Digit Replacer


def digit_replacer(predicate, transformer):
    def replace_digits(n):
        n_str = str(n)
        res_str = ''
        for d in n_str:
            d_int = int(d)
            if predicate(d_int):
                res_str += str(transformer(d_int))
            else:
                res_str += d
        return int(res_str)
    return replace_digits


def is_even(d): return d % 2 == 0
def floor_divide_two(d): return d // 2


print(digit_replacer(is_even, floor_divide_two)(21098))


def lt_five(d): return d < 5
def always_two(d): return 2


print(digit_replacer(lt_five, always_two)(1064592))

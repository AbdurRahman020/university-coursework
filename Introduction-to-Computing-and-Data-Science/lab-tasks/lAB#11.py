"""
LAB # 11: Implementation of Recursion in Python
"""

from IPython import get_ipython
get_ipython().run_line_magic('reset', '-sf')

# %% Q#1


class Snake:
    legs = 0

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def run(self, s):
        print("Snake don't run")
        return self.crawl()

    def crawl(self):
        print(f"{self} crawled")

    def eat(self, s):
        self.run(s)
        print('Nom nom')


class Python(Snake):
    def run(self, s):
        print(eval(s))


snek = Snake('atari')
solidsnake = Snake("David")
solidsnake.legs = 2
solidsnake.run = lambda s: print("He ran")

python = Python('pypy')
print([snek.legs, Snake.legs])
solidsnake.eat("python")
python.eat('snek')
Snake.run(python, python)

# %% Q#2


class Vehicle:
    vehicle_count = 0

    def __init__(self, moving_state: bool):
        self.is_moving = moving_state
        Vehicle.vehicle_count += 1

    def move(self):
        self.is_moving = True

    def brake(self):
        self.is_moving = False

    def __repr__(self):
        return f"{self.__class__.__name__}({self.is_moving})"

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other
        else:
            return False

    @classmethod
    def get_vehicle_count(cls):
        return cls.vehicle_count


v1 = Vehicle(False)
print(v1)

v1.move()
print(v1)

v1.brake()
print(v1)

print(Vehicle(True) == 'Vehicle(True)')

v2 = Vehicle(False)

print(f'No of vehicle = {Vehicle.get_vehicle_count()}')

# %% Q#3


class Car(Vehicle):

    def __init__(self, moving_state, engine):
        super().__init__(moving_state)
        self.engine_state = engine

    def __repr__(self):
        return f"{self.__class__.__name__}({self.is_moving}, {self.engine_state})"

    def StartEngine(self):
        self.engine_state = True


c1 = Car(False, False)
print(c1)

c1.StartEngine()
print(c1)

c1.move()
print(c1)

c1.brake()
print(c1)

print(isinstance(c1, Vehicle))
print(isinstance(v1, Car))

# %% Q#4


class Ratio:

    def __init__(self, x, y):
        self.numertor = x
        self.denmoinator = y

    def __str__(self):
        return f"{self.numertor}/{self.denmoinator}"

    def __mul__(self, other):
        num = self.numertor * other.numertor
        den = self.denmoinator * other.denmoinator
        return Ratio(num, den)

    def scaleBy(self, num):
        return (self.numertor * num)/self.denmoinator


r1 = Ratio(1, 4)
r2 = Ratio(3, 5)

print('r1 = ', r1)

print("r1 * r2 = ", r1 * r2)
print("r2 * r1 = ", r2 * r1)

print("r1 * 3 = ", r1.scaleBy(3))
print("3 * r2 = ", r2.scaleBy(3))

print("r1 * r2 * r1 = ", r1 * r2 * r1)


# %% Q#6

class Gate:

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def numberOfInputs(self):
        return 2

    def setInput(self, idx, state):
        if idx == 0:
            self.x = state
        elif idx == 1:
            self.y = state
        else:
            raise ValueError("invalid input index")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"


class AndGate(Gate):
    def __init__(self, a=False, b=False):
        Gate.__init__(self, a, b)

    def getOutput(self):
        return self.x and self.y


and1 = AndGate()
assert (and1.numberOfInputs() == 2)

and1.setInput(0, True)
and1.setInput(1, False)

assert (str(and1) == "AndGate(True, False)")
assert (and1.getOutput() is False)

and1.setInput(1, True)

assert (and1.getOutput() is True)
assert (str(and1) == "AndGate(True, True)")

# %% Q#7 Code 1


class Chapter:

    def __init__(self, t, p):
        self.title = t
        self.pages = p


class Book:

    def __init__(self, t, c):
        self.title = t
        self.chapters = c
        self.chapterCount = len(self.chapters)

    def getPageCount(self):
        _total = 0
        for x in self.chapters:
            _total += x.pages
        return _total

    def getChapter(self, n):
        return self.chapters[n]

    def moveChapter(self, n, target):
        target.chapters.append(self.chapters[n])
        self.chapters.pop(n)
        self.chapterCount = len(self.chapters)
        target.chapterCount = len(target.chapters)


chapterA = Chapter('I love CS!', 30)
chapterB = Chapter('So do I!', 15)
book1 = Book('CS is Fun!', [chapterA, chapterB])
book2 = Book('The Short Book', [Chapter('Quick Read!', 5)])

assert (book1.chapterCount == 2)
assert (book1.getPageCount() == 45)
assert (book2.chapterCount == 1)
assert (book2.getPageCount() == 5)
assert (book1.getChapter(0).title == 'I love CS!')
assert (book1.getChapter(1).title == 'So do I!')
assert (book2.getChapter(0).title == 'Quick Read!')

book1.moveChapter(0, book2)

assert (book1.chapterCount == 1)
assert (book1.getPageCount() == 15)
assert (book1.getChapter(0).title == 'So do I!')
assert (book2.chapterCount == 2)
assert (book2.getPageCount() == 35)
assert (book2.getChapter(0).title == 'Quick Read!')
assert (book2.getChapter(1).title == 'I love CS!')

# %% Q#7 Code 2


class Person:

    def __init__(self, n, a):
        self.name = n
        self.age = a
        self.l = []

    def getName(self):
        return self.name

    def getFriends(self):
        return self.l

    def getFriendsNames(self):
        self.l1 = []
        for x in self.l:
            self.l1.append(str(x))
        return sorted(self.l1)

    def addFriend(self, n):
        if n not in self.l:
            self.l = self.l + [n]
            n.l = n.l + [self]

    def __str__(self):
        return f'{self.name}'


fred = Person('fred', 32)
assert (isinstance(fred, Person))
assert (fred.getName() == 'fred')

assert (fred.getFriends() == [])
assert (fred.getFriendsNames() == [])

wilma = Person('wilma', 35)
assert (wilma.getName() == 'wilma')
assert (wilma.getFriends() == [])

wilma.addFriend(fred)
assert (wilma.getFriends() == [fred])
assert (wilma.getFriendsNames() == ['fred'])
assert (fred.getFriends() == [wilma])
assert (fred.getFriendsNames() == ['wilma'])

wilma.addFriend(fred)
assert (wilma.getFriends() == [fred])

bob = Person('bob', 35)
wilma.addFriend(bob)
assert (wilma.getFriends() == [fred, bob])
assert (wilma.getFriendsNames() == ['bob', 'fred'])

# %%


class Mint:
    present_year = 2022

    def __init__(self):
        self.update()

    def update(self):
        self.year = Mint.present_year

    def create(self, c):
        return c(self.year)


class Coin:
    cents = None

    def __init__(self, year):
        self.year = year

    def worth(self):
        age = Mint.present_year - self.year

        if isinstance(self, Nickel) and (age > 50):
            return Nickel.cents + (age - 50)
        elif isinstance(self, Dime) and (age > 50):
            return Dime.cents + (age - 50)
        elif isinstance(self, Dime) and (age <= 50):
            return Dime.cents
        elif isinstance(self, Nickel) and (age <= 50):
            return Nickel.cents


class Nickel(Coin):
    cents = 5


class Dime(Coin):
    cents = 10


mint = Mint()
assert (mint.year == 2022)

d = mint.create(Dime)
assert (d.year == 2022)

Mint.present_year = 2102
n = mint.create(Nickel)
assert (n.worth() == 35)

mint.update()
Mint.present_year = 2177
print(mint.create(Dime).worth())
print(Mint().create(Dime).worth())
print(d.worth())

Dime.cents = 20
print(d.worth())

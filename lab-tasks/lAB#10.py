"""
LAB # 10: Implementation of Object-Oriented Programming in Python
"""

import math

# %% Q#1 Code 1


class Car:
    num_of_wheels = 4
    gas = 40
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.wheels = Car.num_of_wheels
        self.gas = Car.gas

    def drive(self):
        if self.wheels < Car.num_of_wheels or self.gas <= 0:
            return "Can't drive"
        self.gas -= 10
        return f"{self.make} {self.model} goes vroom"

    def fillgas(self):
        self.gas += 20
        return f"Gas level: {str(self.gas)}"


class MonsterTruck(Car):
    size = 'Monster'

    def rev(self):
        print("This monster truck is huge!")

    def drive(self):
        self.rev()
        return super().drive()


deneros_car = Car("tesla", "model S")
print(deneros_car.model)

deneros_car.gas = 10
print(deneros_car.drive())
print(deneros_car.drive())
print(deneros_car.fillgas())
print(deneros_car.gas)
print(Car.gas)

deneros_car = Car("tesla", "model S")
deneros_car.wheels = 2
print(deneros_car.wheels)
print(Car.num_of_wheels)
print(deneros_car.drive())

deneros_car = MonsterTruck("Monster", "Batnobile")
print(deneros_car.drive())
print(MonsterTruck.drive(deneros_car))

# %% Q#1 Code 2


class A:
    z = -1

    def f(self, x):
        return B(x-1)


class B(A):
    n = 4

    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y+1)


class C(B):
    def f(self, x):
        return x


a, b = A(), B(1)
b.n = 5
print(C(2).n)
print(a.z == C.z)
print(a.z == b.z)
print(f"b.z = {b.z}\nb.z.z = {b.z.z}\nb.z.z.z = {b.z.z.z}")

# %% Q#1 Code 3


class A:
    def f(self):
        print('a')

    @classmethod
    def g(cls):
        print('b')


A().f()
A.g()
# A.f()

# %% Q#1 Code 4a


class A:
    s = 1


class B(A):
    s = 2


class C(A):
    s = 3


class D(B, C):
    s = 4


print(D().s)

# %% Q#1 Code 4b


class A:
    s = 1


class B(A):
    s = 2


class C(A):
    s = 3


class D(B, C):
    pass


print(D().s)

# %% Q#1 Code 4c


class A:
    s = 1


class B(A):
    pass


class C(A):
    s = 3


class D(B, C):
    pass


print(D().s)

# %% Q#1 Code 4a


class A:
    s = 1


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D().s)

# %% Q#2


class Bird:
    egg_count = 0

    def __init__(self, name):
        self.name = name

    def fly(self):
        return "I can fly"

    def countEggs(self):
        return Bird.egg_count

    def layEggs(self):
        Bird.egg_count += 1

    # def layEggs(self):
    #   egg_count = 0
    #   egg_count += 1
    #   return egg_count


bird1 = Bird("Parrot")
assert (type(bird1) is Bird)
assert (isinstance(bird1, Bird))
assert (bird1.fly() == 'I can fly')
assert (bird1.countEggs() == 0)

bird1.layEggs()
assert (bird1.countEggs() == 1)

bird2 = Bird("Raven")
assert (bird2.countEggs() == 1)

# %% Q#3


class MarksCount:

    def __init__(self, d):
        self.d = d

    def GetMarks(self, k):
        if k in self.d:
            return self.d[k]
        else:
            return None

    def AddMakrs(self, k, score):
        if k in self.d:
            self.d[k] += score

    def GetHighestMarks(self):
        if self.d:
            max_score = max(self.d.values())
            for student, score in self.d.items():
                if score == max_score:
                    return student
        else:
            return None


sb1 = MarksCount({'Alice': 80, 'Bob': 42})
print(sb1.GetMarks('Alice'))
print(sb1.GetMarks('Bob'))
print(sb1.GetMarks('Chee'))

sb1.AddMakrs('Bob', 40)
print(sb1.GetMarks('Bob'))
print(sb1.GetHighestMarks())

# %% Q#4


class Person:

    def __init__(self, name):
        self.name = name
        self._hiList = []

    def sayHi(self, other):
        other._hiList.append(self)

    def saidHiList(self):
        return self._hiList


harry = Person('A')
ron = Person('B')
hermione = Person('C')

hermione.sayHi(ron)

assert (harry.saidHiList() == [])
assert (ron.saidHiList() == [hermione])
assert (hermione.saidHiList() == [])

hermione.sayHi(ron)
harry.sayHi(ron)
ron.sayHi(harry)

assert (harry.saidHiList() == [ron])
assert (ron.saidHiList() == [hermione, hermione, harry])
assert (hermione.saidHiList() == [])

# %% Q#5


class Pet:

    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + 'ate a' + str(thing) + '!')

    def talk(self):
        print(self.name)


class Cat(Pet):

    def __init__(self, name, owner, lives=2):
        Pet.__init__(self, name, owner)
        self.lives = lives

    def talk(self):
        print(f"{self.name} say's meow!")

    def lost_life(self):
        if self.lives > 0:
            self.lives -= 1
            print(f"{self.name} has {self.lives} lives left.")
            if self.lives == 0:
                self.is_alive = False
                print(f"{self.name} has no more lives i.e. the {
                      self.name} is dead.")
        else:
            print("This cat has no more lives to lose.")


class NoisyCat(Cat):

    def __init__(self, name, owner, lives=9):
        Cat.__init__(self, name, owner, lives)

    def talk(self):
        super().talk()
        super().talk()


Cat('Thomas', 'Tammy').talk()
NoisyCat('Magic', 'James').talk()

# for classes in reversed(NoisyCat.mro()):
#    print(classes)

# %% Q#6


class ComplexRI:

    def __init__(self, real, imag):
        self.x = real
        self.y = imag

    def real(self):
        return self.x

    def imaginary(self):
        return self.y

    def magnitude(self):
        # r = sqrt(x**2 + y**2)
        return math.hypot(self.x, self.y)

    def angle(self):
        # theta = arctan(y/x)
        angle = math.atan2(self.y, self.x)
        return angle if angle >= 0 else 2 * math.pi + angle

    def __add__(self, other):
        if isinstance(other, ComplexRI):
            return ComplexRI(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported type for addition with ComplexRI")

    def __str__(self):
        return f'{self.x} ' + ('+' if self.y >= 0 else '-') + f' {abs(self.y)}i'


c1 = ComplexRI(5, 2)
c2 = ComplexRI(-5, 2)
c3 = ComplexRI(-5, -2)
c4 = ComplexRI(5, -2)

print(c3)

l = [c1, c2, c3, c4]

for x in l:
    print(f'mag = {x.magnitude()}')
    print(f'ang = {x.angle()}')

# %% Q#7


class ComplexMA:

    def __init__(self, mag, ang):
        self.r = mag
        self.theta = ang * math.pi/180

    def real(self):
        # x = r * cos(theta)
        return self.r * math.cos(self.theta)

    def imaginary(self):
        # y = r * sin(theta)
        return self.r * math.sin(self.theta)

    def __add__(self, other):
        if isinstance(other, ComplexMA):
            return ComplexMA(self.r + other.r, math.degrees(self.theta + other.theta))
        else:
            raise TypeError("Unsupported type for addition with ComplexMA")

    def __str__(self):
        return f'{self.r:.2f} < {math.degrees(self.theta):.2f}°'


c1 = ComplexMA(18.02, 5.695)
print(c1)
print(c1.real())
print(c1.imaginary())

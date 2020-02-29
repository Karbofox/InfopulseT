# class Person:
#     scope = ['people', 'something']
#
#     def __init__(self, name="", age=None, position=None):
#         self.name = name
#         self.age = age
#         self.position = position
#
#     def __add__(self, other):
#         return Person(self.name + other.name,1,2)
#
#     def __str__(self):
#         #return self.name + '-' + self.age
#         return f"Person with name {self.name}"
#
#     def set_name(self, x):
#         self.name = x
#
#
#
#
#
#
# p1 = Person("Olya", 25, "QA")
# p2 = Person("Kolya", 25, "QA")
#
# print((p1+p2).name)

# p1 = Person()
# #print(p1)
# p1.set_name('Vasya11111111111111')
# print(p1.name)
#
# p2 = Person()
# #print(p2)
# p2.set_name('Vasya11111111111111')
# print(p2.name)
#
# print(p1.name is p2.name)

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def full_name(self):
        return self.name + ' ' + self.surname

    def get_older(self, years):
        self.age += years


# p1 = Person("Peter", "Jacobson", 12)
# print(p1.full_name())
#
# p1.get_older(5)
# print(p1.age)


# class Employee(Person):
#
#     def __init__(self, name='', surname='', age=None, position=None, salary=0):
#         Person.__init__(self, name, surname, age)  # self - Employee, not Person
#     #super().__init__(name, surname, age)
#
#
#
#     def get_older(self, years):
#         self.age += years
from math import sqrt

class Rectangular:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        return self.a*self.b

    def prm(self):
        return 2*(self.a+self.b)


class Dot:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return sqrt(self.x**2+self.y**2)

    def new_coords(self, x, y):
        return

import unittest
from HomeTask3.HomeTask3_6 import is_year_leap


class TestLeapYear(unittest.TestCase):

    def test_leap_year(self):
        year = 2000
        res = is_year_leap(year)
        self.assertTrue(res)

    def test_zero_year(self):
        year = 0
        res = is_year_leap(year)
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()

# l = ["asd", "ff", "wgggggg", "dsfsfsdf"]
#
# i = 0
# for each in l:
#     if len(each)%2 == 1: i+= 1
#
# print(i)


#dct = {"key1":1,"key2":22,"key3":4444}
#print(dct.items(),sep="\n")
# for each in dct:
#      print(each,dct.get(each),type(each),type(dct.get(each)),sep=":")

# for each in dct.keys():
#     print(each,dct[each],sep=":")

#for each in dct:
#    print(each,dct[each],sep=":")


# print(10)
# raise ValueError("bla-bla-bla")
# print("Executed?")
#

# a = input("String: ")
# assert len(a)<10
# print(a)

# def word_printer(word, count=1, wow=0):
#     if wow == 1:
#         return (word*count).upper()
#     else:
#         return word * count
#
#
# print(word_printer("Bob",wow=1,count=3))


#
# def func(*args):
#     print(type(args))


# def word_counter(**word):
#     return word

#
# def func(a,b,c,d):
#     return (a-b)*c/d
# d = {"a":5,"b":1,"c":4,"d":2}
# l = [5,1,4,2]
#
# print(func(*l))
# print(func(**d))
#
# l = ["John","Lilly","Ann"]
# print(*l)
# print(l)
#
# import math
# print(math.pi)
#
# from math import pi
# print(pi)

# from sys import *

from HomeTask3.HomeTask3_6 import inputNumber
x = inputNumber()
print(x)
#Task 2 ----------------------------------------------------------
import math
s1 = input("Input the string: ")
n = math.ceil(len(s1)/2)
s11 = s1[n:]+s1[:n]
print(s11)
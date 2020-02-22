# Task 5 ----------------------------------------------------------
a = input("Enter first value: ")
b = input("Enter second value: ")
res = ''

try:
    res = float(a)+float(b)
except ValueError:
    res = a+b
finally:
    print(res)
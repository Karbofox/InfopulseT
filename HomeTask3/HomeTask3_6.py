# Task 6.1 ----------------------------------------------------------
def inputNumber(s = 'the number'):
    s = "Enter "+ s +": "
    while True:
        try:
            return(float(input(s)))
        except ValueError:
            continue

# Task 6.2 ----------------------------------------------------------
def inputWord():
    while True:
        s = input("Enter single word: ")
        if s.strip().count(' ') == 0:
            return s
        else:
            continue

# Task 6.3 ----------------------------------------------------------
def is_year_leap(year):
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        return True
    else:
        return False

# Task 6.4 ----------------------------------------------------------
def isTriangle(a,b,c):
    return 2*max(a,b,c) < (a+b+c)

# Task 6.5 ----------------------------------------------------------

def numberOfEqual(a, b, c):
    l = [a, b, c]
    n = max(l.count(a),l.count(b),l.count(c))
    return n if n > 1 else 0

def triagleType(a, b, c):
    if not isTriangle(a,b,c):
        print("Not a triangle")
    elif numberOfEqual(a,b,c) == 0:
        print("Versatile triangle")
    elif numberOfEqual(a,b,c) == 2:
        print("Isosceles triangle")
    elif numberOfEqual(a,b,c) == 3:
        print("Equilateral triangle")

# triagleType(0,0,0)
# triagleType(1,2,2)
# triagleType(2,2,2)
# triagleType(2,12,13)
# triagleType(-1,2,2)

#Task 6.6 ----------------------------------------------------------
from math import sqrt
def distance(x1,y1,x2,y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

x1 = inputNumber("x1")
y1 = inputNumber("y1")
x2 = inputNumber("x2")
y2 = inputNumber("y2")
print(distance(x1,y1,x2,y2))
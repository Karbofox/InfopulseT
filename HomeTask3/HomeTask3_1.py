# Task 1 ----------------------------------------------------------
s = input("Input the string: ")
try:
    print(s[2],
      s[-2],
      s[:5],
      s[:-2],
      s[::2],
      s[1::2],
      s[-1::-1],
      s[-1::-2],
      s[-2::-2],
      s[-2:0:-1],
      len(s),
      sep='\n')
except IndexError:
    print("The string entered is too short")
# s = input('Enter text: ')
# if s == "Hi":
#     print("Hello")
# print("Goodbye")

# f = float(input('Enter the number: '))
# print('Correct number') if f>0 and f<=100 else print('Incorrect number')
#
# l = [1,3,[1,4],5,6,7]
# while l:
#     print(l.pop())


# print(l)
#
# k = 0
# x = 4
# while x%2 == 0:
#     x = x/2
#     k+=1
# print(k)
#
# even = []
# odd = []
# l = [1,3,1,4,5,6,7,7]
# for item in l:
#     if item % 2 == 0: print(item)
#     else: print(item+1)
#

#l = [1,3,1,4,5,6,7,7]

# for i in range(
# len(l)):
#     if l[i]%2 == 1: l[i]+=1
# print(l)
#

#l = list(range(10))
#print(l)

# s = ' '
# while s.count(' '):
#     s = input("Enter string: ")


# while s.strip().count(' '):
#     s = input("Enter string: ")

#s,i = 'a', 0
# try:
#     s = int(s) / i
# except ValueError as e:
#     print(e)
# except  ZeroDivisionError:
#     print(' / 0')

# while True:
#     try:
#         f = float(input('Enter the number: '))
#     except ValueError as e:
#         continue
#     else:
#         break
# print(type(f))


def func():
    while True:
        try:
            f = float(input('Enter the number: '))
        except ValueError:
            func()
        else:
            return f

print(func())
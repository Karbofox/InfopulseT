print("Task 3.1 ----------------------------------------------------------")
i = 0
while i < 11:
    print(i)
    i += 1

print("Task 3.2 ----------------------------------------------------------")
i = 20
while i > 0:
    print(i,end=' ')
    i -= 1

print("\nTask 3.3 ----------------------------------------------------------")
k = 2
print("For k =",k, end="")
if k%2 == 0:
    i = 0
    while k%2 == 0:
        k /= 2
        i += 1
print(" the number of division operations is", i)
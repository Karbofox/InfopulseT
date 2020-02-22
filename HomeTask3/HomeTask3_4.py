print("Task 4.1 ---------------------------")
l = [1,10,3,2,1,5,4]
print(l)
while l:
    print(l.pop(0))

print("Task 4.2 ---------------------------")
s = 'abcdefgh'
print(s)
while s:
    print(s[0])
    s=s[1:]

print("Task 4.3 ---------------------------")
l = [1,10,3,2,1,5,4]
print(l)
l.sort()
while l:
    print(l.pop(0))

print("Task 4.4 ---------------------------")
l = [1,3,3,1,1,1,4,4,0]
print(l)
mx = 0
i = 0
while l and l[1] != 0:
     if l[1] == l.pop(0):
         i += 1
         mx = max(mx, i+1)
     else:
         i = 0
print("The maximum length of sequence of the equal elements is",mx)
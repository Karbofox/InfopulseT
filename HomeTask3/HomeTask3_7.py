# Task 7 ----------------------------------------------------------
s = "We are not what we should be!\n " \
    "We are not what we need to be.\n " \
    "But at least we are not what we used to be.\n " \
    "(Football Coach)"

l = s.split(sep=' ')

print("Number of words:", len(l))
for i in range(len(l)):
    l[i] = l[i].strip(' ,.!?:;()\n')
print("list of words without separators:\n",l)

for i in range(len(l)):
    l[i] = l[i].lower()
l.sort()
print("Sorted list:\n",l)

i = 0
dct = dict()
while i < len(l):
    dct[l[i]] = l.count(l[i])
    i += l.count(l[i])
print("Word : count \n",dct)



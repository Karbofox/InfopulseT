#Task 1
from math import sqrt
a = 158
b = 971
print('Task #1')
print('For a=', a,'and b=',b,' c is',sqrt(a**2+b**2),'\n')

#Task 2
c = 45
print('Task #2')
print('Number of tens in',c,'is ',c//10,'\n')

#Task 3
d = 417
print('Task #3')
print('Sum od digits for',d,'is ',d//100+(d-100*(d//100))//10+d%10,'\n')

#Task 4
e = 1
print('Task #4')
print('The next even for',e,'is ',2*(e//2)+2,'\n')

#Task 5
f = 15.99
print('Task #5')
print('The fraction for',f,'is ',f-int(f),'\n')

#Task 6
f = 15.01
print('Task #6')
print('First digit after "." for',f,'is ',int(f*10)-10*(int(f)),'\n')
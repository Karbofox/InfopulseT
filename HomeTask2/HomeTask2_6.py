l = list()
#a = int(input('Input a: '))
l.append(int(input('Input a: ')))
#b = int(input('Input b: '))
l.append(int(input('Input b: ')))
#c = int(input('Input c: '))
l.append(int(input('Input c: ')))

n = max(l.count(l[0]),l.count(l[1]),l.count(l[2]))

print(n) if n > 1 else print('0')


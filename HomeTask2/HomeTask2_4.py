a = 12
b = 15
c = 26.9999999
if (a <= 0 or b <= 0 or c <= 0 or
        2*max(a,b,c) >= (a+b+c)):
    print("NO")
else:
    print("YES!")
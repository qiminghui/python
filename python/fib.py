def fib(max):
    n,a,b = 0,0,1
    while n < max :
        a,b = b,a+b
        print(b)
        n += 1
(fib(4))
l = []
for i in range(5):
    if i == 0 or i == 1:
        l.append(i)
    else:
        l.append(l[i-2]+l[i-1])
print(l)

a = 1.0
b = 2.0
s = 0
for n in range(20):
    s += a/b
    a,b = b,a+b
print(s)
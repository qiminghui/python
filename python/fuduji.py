a = input("the add number:")
b = int(input("how much"))
res = 0 
for i in range(b):
    res += int(a)
    a += a[0]
print(res)
def fa(n):
    if n ==1 :
        return 1
    else:
        return n*fa(n-1)
print(fa(3))

def age(n):
    if n == 1:
        return 10
    else:
        return 2 + age(n-1)
print(age(5))
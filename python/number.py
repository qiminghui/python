i = 1
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            if ((x != y)and(x != z)and(y != z)):
                if i % 4:
                    print("%d%d%d" % (x,y,z),end = '|')
                else:
                    print("%d%d%d" % (x,y,z))
                i += 1
print(i)
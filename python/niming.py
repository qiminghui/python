i = 0
for x in range(1, 6):
    for y in range(1, 6):
        for z in range(1, 6):
            if (x != y) and (y != z) and (z != x):
                i += 1
                if i % 4:
                    print("%d%d%d" % (x, y, z), end=" | ")
                else:
                     print("%d%d%d" % (x, y, z))
print(i)
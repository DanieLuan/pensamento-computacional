n = int(input('n?'))
i1 = 0
i2 = 1
i3 = 2
while n != (i1 * i2 * i3):
    i1 += 1
    i2 += 1
    i3 += 1
    if (i1 * i2 * i3) > n:
        print('não é triangular')
        break
if (i1 * i2 * i3) == n:
    print('é triangular')
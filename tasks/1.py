n = int(input())

for i in range(2, n):
    for j in range(2, i+1):
        if i % j == 0 and i / j != 1:
            break
        elif i % j != 0:
            continue
        else:
            print(i, end=' ')


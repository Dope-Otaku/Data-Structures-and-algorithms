'''

1
01
101
0101
10101

we need to implement this...

'''
n = 5

for i in range(n):
    m = i%2
    for j in range(i+1):
        if m == 0:
            print("1", end="")
            m = 1
        else:
            print("0", end="")
            m = 0
    print()
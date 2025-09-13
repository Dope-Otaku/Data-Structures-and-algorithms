'''
A
BB
CCC
DDDD
EEEEE

we need to implement this
'''


n = 5

for i in range(1, n+1):
    ase = ord('A') + (i-1)
    for j in range(i):
        print(chr(ase), end="")
    print()
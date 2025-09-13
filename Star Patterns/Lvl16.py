'''


E
DE
CDE
BCDE
ABCDE

we need to implement this
'''

n =5

for i in range(1, n+1):
    ase = ord('E') - (i-1)
    for j in range(ase, ord('E') + 1):
        print(chr(j), end="")
        ase = ase-1
        
    print()


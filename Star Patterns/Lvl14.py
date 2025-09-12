'''


a
ab
abc
abcd
abcde

we need to implement this
'''

n =5
# ase = ord('A')

for i in range(1, n+1):
    ase = ord('A')
    for j in range(i):
        print(chr(ase), end="")
        ase = ase+1
        
    print()
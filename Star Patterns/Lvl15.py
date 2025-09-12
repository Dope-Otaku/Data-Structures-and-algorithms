'''
ABCDE
ABCD
ABC
AB
A

we need to implement this

'''


n =5

for i in range(1, n+1):
    ase = ord('A')
    for j in range(n-i, -1, -1):
        print(chr(ase), end="")
        ase = ase+1
        
    print()
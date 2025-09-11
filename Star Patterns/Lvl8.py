'''
*********
 *******
  *****
   ***
    *

we need to implement this in our code
'''


n = 9 

for i in range(n):
    for j in range(0, i):
        print(" ", end="")
    for j in range(n-2*i, 0, -1):
        print("*", end="")
    print()
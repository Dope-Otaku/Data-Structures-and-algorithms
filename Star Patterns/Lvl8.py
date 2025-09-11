'''
*********
 *******
  *****
   ***
    *

we need to implement this in our code
'''


n = 5 

for i in range(n):
    for j in range(0, i):
        print(" ", end="")
    for j in range(n-i, 0, -1):
        print("*", end="")
    print()
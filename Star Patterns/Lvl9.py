'''
    *    
   ***   
  *****  
 ******* 
*********
*********
 *******
  *****
   ***
    *


we need to implement this in code

'''

n = 5

for i in range(n):
    #space
    for j in range(0, n-i-1):
        print(" ", end="")
        # print("space 1")
    #star
    for j in range(2*i+1):
        print("*", end="")
    print()

# n = 9 

for i in range(n):
    for j in range(0, i):
        print(" ", end="")
    for j in range(2*(n-i)-1):
        print("*", end="")
    print()
'''
    *    
   ***   
  *****  
 ******* 
*********

we need to solve this pattern uhhh

'''

n = 5

for i in range(n):
    #space
    for j in range(0, n-i, -1):
        print(" ", end="")
    #star
    for j in range(2*n+1):
        print("*", end="")
    #space
    for j in range(0, n-i, -1):
        print(" ", end="")
    print()
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
    for j in range(n-i+1):
        print(" ", end="")
    #star
    for k in range(2*n+1):
        print("*", end="")
    #space
    for l in range(n-i+1):
        print(" ", end="")
    print()
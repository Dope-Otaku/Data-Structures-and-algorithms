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
        print(" ")
        print("space 1")
    #star
    for j in range(2*i+1):
        print("*", end="")
    #space
    for j in range(0, n-i, -1):
        print(" ")
        print("space 2")
    print()
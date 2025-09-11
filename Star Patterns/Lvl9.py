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

n = 10
m = int(n/2)


for i in range(n):
    for j in range(m):
        for a in range(0, m-i):
            print(" ", end="")
            # print("space 1")
        #star
        for b in range(2*j+1):
            print("*", end="")
    print()
    for k in range(m):
        for c in range(0, k):
            print(" ", end="")
        for d in range(m-2*k, 0, -1):
            print("*", end="")
    print()






# for i in range(n):
#     for j in range(0, i):
#         print(" ", end="")
#     for j in range(n-2*i, 0, -1):
#         print("*", end="")
#     print()

# for k in range(n):
#     for l in range(0, i):
#         print(" ", end="")
#     for l in range(n-2*i, 0, -1):
#         print("*", end="")
#     print()
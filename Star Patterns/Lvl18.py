'''
   A
  ABA
 ABCBA
ABCDCBA

we need to implement this

'''

n = 5

for i in range(n):
    # for spaces
    for j in range(n-i):
        print(" ", end="")
    
    #for content after space
    for j in range(2*i+1):
        print("x")

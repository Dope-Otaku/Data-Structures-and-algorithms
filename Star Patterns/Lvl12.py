'''
1      1
12    21
123  321
12344321


we need to implement this pattern

'''

n = 4

for i in range(1, n+1):
    # first character
    for j in range(1, i+1):
        print(j, end="")
    #spaces between them
    for j in range(2*(n-i)):
        print(" ", end="")
        # print("-", end="")
    #second characters
    for j in range(i, 0, -1):
        print(j, end="")
    print()
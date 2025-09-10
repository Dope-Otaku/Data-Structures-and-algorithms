'''

12345
1234
123
12
1


we need to implement this pattern


'''

n = 5

for i in range(n):
    for j in range(n-i):
        print(j+1, end="")
    print()
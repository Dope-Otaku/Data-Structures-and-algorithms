'''

1
12
123
1234
12345

we need to replicate this 

'''



n = 5

for i in range(1,n):
    for j in range(i):
        print(j+1, end="")
    print()
'''

1
23
456
78910
1112131415

we need to implement this
'''

n =5
w = 1

for i in range(1, n+1):
    for j in range(i):
        print(w, end="")
        w+=1
    print()
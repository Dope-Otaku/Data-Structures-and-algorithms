# can place flowers

listm = [1,0,0,0,1]
l = 2
n = [0] + listm + [0]
for i in range(len(n)):
    if n[i-1]==0 and n[i] == 0 and n[i+1]==0:
        n[i] = 1
        l -= 1
print(l<=0)
print(f"new flowerbed is: {n}")
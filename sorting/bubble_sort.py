t = [50, 20, 37, 91, 64, 18, 43, 59, 72, 81]

compared_value = len(t) -1 #this many times the operation will run
count = 0
left = 0
right = 1


while count >=0 and count <= compared_value:
    if t[left] > t[right]:
        t[left], t[right] = t[right], t[left]
        left += 1
        right += 1
    elif t[left] < t[right]:
        left += 1
        right += 1
    count += 1
    

print(t)
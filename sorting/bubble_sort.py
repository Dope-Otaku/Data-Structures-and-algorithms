t = [24, 58, 11, 67, 92, 43]

compared_value = len(t)  #this many times the operation will run
count = 0
left = 0
right = 1


while count >=0 and count < compared_value:
    if t[left] > t[right]:
        print(f"left:{t[left]}, right:{t[right]}")
        t[left], t[right] = t[right], t[left]
        left += 1
        right += 1
    elif t[left] < t[right]:
        left += 1
        right += 1
    count += 1
    

print(t)
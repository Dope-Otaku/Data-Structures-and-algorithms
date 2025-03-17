t = [24, 58, 11, 67, 92, 43]

compared_value = len(t)  #this many times the operation will run
count = 0
left = 0
right = 1


while count < compared_value - 1:
    while right < compared_value:
        if t[left] > t[right]:
            print(f"left:{t[left]}, right:{t[right]}| {t}")
            t[left], t[right] = t[right], t[left]
        left += 1
        right += 1
             
    left = 0
    right = 1
    count += 1
    

print(t)



# t = [24, 58, 11, 67, 92, 43]

# compared_value = len(t)  # This is the number of elements in the list
# count = 0

# # Bubble Sort Loop
# while count < compared_value - 1:  # We need len(t)-1 iterations
#     for i in range(compared_value - 1 - count):  # Perform n-1 comparisons per iteration
#         if t[i] > t[i + 1]:  # If the current element is greater than the next
#             print(f"Swapping: left:{t[i]}, right:{t[i+1]} | {t}")
#             t[i], t[i + 1] = t[i + 1], t[i]  # Swap the elements
#     count += 1

# print(f"Sorted list: {t}")

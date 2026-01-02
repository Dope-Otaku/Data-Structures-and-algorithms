# Given an integer N, return the number of digits in N.


n = 4578

#first mistake len() function is only available for arrray and string data type
#second mistake learned that int value mai loop nahi laga sakte
a = n
flag = 0
while a > 0:
    # last = a%10
    flag+=1
    a = a//10
print(flag)



'''.   so let's say what if we have a string we can use len built in function but i want to create of my own '''

val = [1,2,2]
count = 0
for chr in val:
    count +=1
print(count)

# m = n
# count = 0


# while m > 0:
#     last_digit = m%10
#     count +=1
#     m = m//10

# print(count)

# #solved


# #optimal approach
# # completed


# import math

# a = n

# def count_digi(a):
#     cnt = math.log10(a) +1
#     return cnt

# print(count_digi(a))





#hi i have an update on this new year so from today on we will be pulling on a new self and be consistent throught whole year i promise
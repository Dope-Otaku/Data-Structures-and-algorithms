# Given an integer N, return the number of digits in N.


n = 4578

m = n
count = 0


while m > 0:
    last_digit = m%10
    count +=1
    m = m//10

print(count)
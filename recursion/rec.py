#we will learn recursion through questions

#q.1 write a recursion function to print first N natural numbers

# def natural(n):
#     if n > 0:
#         natural(n-1)
#         print(n, end=' ')

# print(natural(5))

#q.2 write a recursion function to print first N natural numbers in reverse order

# def natural(n):
#     if n > 0:
#         print(n, end=' ')
#         natural(n-1)

# print(natural(5))

#q.3 write a recursive fnction to print first N odd natural numbers

def odd(n):
    if n>0:
        odd(n-1)
        print(2*n-1, end=' ')

print(odd(10))
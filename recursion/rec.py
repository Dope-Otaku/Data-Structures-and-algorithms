#we will learn recursion through questions

#q.1 write a recursion function to print first N natural numbers

# def natural(n):
#     if n > 0:
#         natural(n-1)
#         print(n, end=' ')

# print(natural(5))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))





#q.2 write a recursion function to print first N natural numbers in reverse order

# def natural(n):
#     if n > 0:
#         print(n, end=' ')
#         natural(n-1)

# print(natural(5))

#q.3 write a recursive fnction to print first N odd natural numbers

# def odd(n):
#     if n>0:
#         odd(n-1)
#         print(2*n-1, end=' ')

# print(odd(10))

#q.4 write a recursive fnction to print first N even natural numbers

# def even(n):
#     if n>0:
#         even(n-1)
#         print(2*n, end=' ')

# print(even(10))

#q.5 write a recursive fnction to print first N odd natural numbers in reverse order

# def odd(n):
#     if n>0:
#         print(2*n-1, end=' ')
#         odd(n-1)

# print(odd(10))

#q.6 write a recursive fnction to print first N even natural numbers in reverse order

# def even(n):
#     if n>0:
#         print(2*n, end=' ')
#         even(n-1)

# print(even(10))

#q.7 write a recursive function to calculate sum of first N natural numbers

# def sum(n):
#     if n <= 0:
#         return 0
#     s = sum(n-1) + n
#     return s
    
# print(sum(5))

#q.8 write a recursive function to calculate sum of first N odd natural numbers

# def num(n):
#     if n == 1:
#         return 1
    
#     s = num(n-1) + (2*n-1)
#     return s
    
# print(num(10))

#q.9 write a recursive function to calculate sum of first N even natural numbers

# def num(n):
#     if n == 1:
#         return 2
    
#     s = num(n-1) + (2*n)
#     return s
    
# print(num(2))

#q.10 write a recursive function to calculate factorial of a number

# def factorial(n):
#     if n==0:
#         return 1
#     return factorial(n-1) * n

# print(factorial(4))

#q.11 write a recursive function to calculate sum of squares of firrst N natural numbers

# def sq(n):
#     if n == 0:
#         return 0
#     return sq(n-1)+n**2

# print(sq(5))
#we will learn recursion through questions

#q.1 write a recursion function to print first N natural numbers

# def natural(n):
#     if n > 0:
#         natural(n-1)
#         print(n, end=' ')

# print(natural(5))

#q.2 write a recursion function to print first N natural numbers in reverse order

def natural(n):
    if n > 0:
        print(n, end=' ')
        natural(n-1)

print(natural(5))
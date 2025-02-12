# x = [18, 43, 36, 13, 7]


'''
hint - group all the numbers which have same sum
'''
x = [18, 43, 36, 13, 7]


# first part completed of internal int adding
def internalAdder(nums):
    # return sum[int(d) for d in str(nums)]
    # print(sum(int[d] for d in str(nums)))
    return sum([int(d) for d in str(nums)])
    



def maxSum(x):
    numberMap = {}
    maxSum = -1

    for value in x:
        digitSum = internalAdder(value)
        print(digitSum)

print(maxSum(x))

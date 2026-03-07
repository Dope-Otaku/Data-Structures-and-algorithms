'''
Fixed size sliding window implementation in Python.

given an array nums consisted  of only non-negative integers, find the largest
sum among all subarrays of length k in nums

for example: nums = [1,2,3,7,4,1], k =3, output = 14 ,[3,4,7]

'''

nums = [1,2,3,7,4,1]
k =3

def subarray_sum_fixed(input, window_size):
    ans = window = input[0:window_size]
    highV = []
    for right in range(window_size, len(input)):
        left = right - window_size
        window.remove(input[left])
        window.append(input[right])
        highV.append(sum(window))

        ans = max(highV)
    return ans

print(subarray_sum_fixed(nums, k))
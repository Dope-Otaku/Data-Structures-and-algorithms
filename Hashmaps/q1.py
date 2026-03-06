'''
two sum question:

given an array of integers nums and an integer target,
return the indices of the two numbers such that they
add up to target. you may assume that each input would 
have exactly one solution and you may not use the same element twice 

example: 

input: nums = [2,7,11,15], target = 9
output : [0,1]
explanation: because nums[0] + nums[1] == 9, we return [0,1]

'''


nums = [2,7,11,15]

target = 9


def two_sum(nums):
    num_to_index = {}

    for i, num in enumerate(nums):
        comp = target - num
        if comp in num_to_index:
            return [num_to_index[comp], i]
        num_to_index[num] = i

print(two_sum(nums=nums))

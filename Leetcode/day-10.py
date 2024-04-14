#  Move Zeroes
# class Solution(object):
#     def moveZeroes(self, nums):
#         insert_pos = 0
        
#         for num in nums:
#             if num != 0:
#                 nums[insert_pos] = num
#                 insert_pos += 1
        
#         while insert_pos < len(nums):
#             nums[insert_pos] = 0
#             insert_pos += 1




# my own solution
nums = [0, 1, 0, 3, 12]

i = 0
j = 1

while j < len(nums):
    if nums[i] == 0 and nums[j] != 0:
        nums[i], nums[j] = nums[j], nums[i]
    if nums[i] != 0:
        i += 1
    j += 1

print(nums)

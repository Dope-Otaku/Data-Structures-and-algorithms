nums = [1,12,-5,-6,50,3]
k = 4

print(max(nums))

# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         currSum = 0
#         for i in range(k):
#             currSum += nums[i]
#         maxSum = currSum # assume max sum is the sum of first 'k' elements
#         left = 0
#         right = k
#         while right < len(nums): # sliding window
#             currSum -= nums[left] # remove left element's value from sum
#             left += 1 # shift left index
#             currSum += nums[right] # add right element's value to sum
#             right += 1 # shift right index
#             maxSum = max(maxSum, currSum) # check if currSum > maxSum
#         return maxSum / k # return the average
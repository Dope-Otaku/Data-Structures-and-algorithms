#  Increasing Triplet Subsequence
# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         first = second = float('inf') 
#         for n in nums: 
#             if n <= first: 
#                 first = n
#             elif n <= second:
#                 second = n
#             else:
#                 return True
#         return False


#my own logic after watching explanation
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1, num2 = inf, inf
        for num3 in nums:
            if num3<= num1:
                num1 = num3
            elif num3<=num2:
                num2 = num3
            else:
                return True
        return False
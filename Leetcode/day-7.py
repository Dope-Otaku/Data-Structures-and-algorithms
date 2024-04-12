#product of array except self

#approach = we will first traverse from left to right and then right to left with one space leaving for each at start

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]

        rp = 1 #rp = rightproduct

        for i in range(n-1, -1, -1):
            ans[i] = ans[i] * rp
            rp = rp * nums[i]
        return ans  
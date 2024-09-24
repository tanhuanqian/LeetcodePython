class Solution(object):
    def maxSubArray(self, nums):
        maxcurrent = maxglobal = nums[0]
        n = len(nums)
        for i in range(1,n):
            maxcurrent = max(nums[i], maxcurrent+nums[i])
            print(maxcurrent, i)
            if maxcurrent > maxglobal:
                maxglobal = maxcurrent
        return maxglobal
nums = [-2,5,-3,4,-1,2,1,-3,4]
solution = Solution()
print(solution.maxSubArray(nums))
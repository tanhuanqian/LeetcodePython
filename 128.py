class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        n = len(nums)
        curr = 1
        maxlength = 1
        for i in range(n-1):
            if nums[i+1] - nums[i] != 1:
                maxlength = max(maxlength, curr)
                curr = 1
            elif nums[i+1] - nums[i] == 1:
                curr += 1
        maxlength = max(maxlength, curr)
        return maxlength
    
nums = [1, 2, 3, 4, 7, 8, 9]
solution = Solution()
print(solution.longestConsecutive(nums))
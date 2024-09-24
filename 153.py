class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

nums = [1,2,3,4,5,0]       
solution = Solution()
print(solution.findMin(nums))
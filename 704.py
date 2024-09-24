class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (r)//2
            if nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                return mid
        return -1
    
nums = [-1,0,3,5,9,12]
solution = Solution()
print(solution.search(nums, 9))
class Solution(object):
    def search(self, nums, target):
        left = 0
        right =len(nums)-1
        while left <= right:
            mid = (left+right)//2
            print(left,mid,right, nums[mid])
            if target == nums[mid]:
                return mid
            elif nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
        return -1
    
nums = [4,5,6,7,0,1,2]    
solution = Solution()
print(solution.search(nums, 0))
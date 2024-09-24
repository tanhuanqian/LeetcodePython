from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        res = []
        dq = deque()
        for i in range (n):
            if dq and dq[0] < i-k+1:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                res.append(nums[dq[0]])
        return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
solution = Solution()
print(solution.maxSlidingWindow(nums,k))
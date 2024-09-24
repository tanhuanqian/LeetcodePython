class Solution(object):
    def maximumSubarrayXor(self, nums, queries):
        n = len(nums)
        f = [[0]* n for _ in range(n)]
        mx = [[0]* n for _ in range(n)]
        for i in range(n-1, -1, -1):
            mx[i][i] = f[i][i] = nums[i]
            for j in range(i+1, n):
                f[i][j] = f[i][j-1]^ f[i+1][j]
                mx[i][j] = max(f[i][j], mx[i+1][j], mx[i][j-1])
        return [mx[l][r] for l,r in queries]

nums = [2,8,4,32,16,1]
queries = [[0,2],[1,4],[0,5]]
solution = Solution()
print(solution.maximumSubarrayXor(nums, queries))
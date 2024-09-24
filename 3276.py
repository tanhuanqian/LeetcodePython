from functools import lru_cache,cache
class Solution(object):
    def maxScore(self, grid):
        mx = max(map(max,grid))
        pos = [[] for _ in range (mx+1)]
        for i, row in enumerate(grid):
            for x in set(row):
                pos[x].append(i)

        @cache
        def dfs(i: int, j:int) -> int:
            if i == 0:
                return 0
            res = dfs(i-1, j)
            for k in pos[i]:
                if(j >> k & 1) == 0:
                    res = max(res, dfs(i-1, j|1 << k)+i)
            return res
        return dfs(mx,0)
    
grid = [[1,2,3],[4,3,2],[1,1,1]]
solution = Solution()
print(solution.maxScore(grid))
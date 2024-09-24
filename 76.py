from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        i, n, l = 0, len(s), len(t)
        mn = float('inf')
        counters = Counter(s[:l])
        countert = Counter(t)
        print(counters, countert)
        for j in range (l, n-1):
            if set(t).issubset(set(s)):
                mn = min(mn, j-i)
                


s = "ADOBECODEBANC"
t = "ABC"
solution = Solution()
print(solution.minWindow(s, t))
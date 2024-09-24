class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""
        dictT = {}
        for c in t:
            dictT[c] = dictT.get(c, 0) + 1
        required = len(dictT)
        l, r = 0, 0
        formed = 0
        windowCounts = {}
        ans = [-1, 0, 0]
        while r < len(s):
            c = s[r]
            windowCounts[c] = windowCounts.get(c, 0) + 1
            if c in dictT and windowCounts[c] == dictT[c]:
                formed += 1
            while l <= r and formed == required:
                c = s[l]
                if ans[0] == -1 or r - l + 1 < ans[0]:
                    ans[0] = r - l + 1
                    ans[1] = l
                    ans[2] = r
                windowCounts[c] -= 1
                if c in dictT and windowCounts[c] < dictT[c]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == -1 else s[ans[1]: ans[2] + 1]
s = "ADOBECODEBANC"
t = "ABC"
solution = Solution()
print(solution.minWindow(s, t))
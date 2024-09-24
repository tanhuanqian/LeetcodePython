class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        maxlen = 0
        i = 0
        for j in range (len(s)):
            if s[j] in seen:
                i = max(i, seen[s[j]]+1)
            seen[s[j]] = j
            maxlen = max(maxlen, j-i+1)
        return maxlen
s = "abcabcbb"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))
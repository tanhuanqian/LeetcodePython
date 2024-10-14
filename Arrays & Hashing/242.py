class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s)==sorted(t)
    
sol = Solution()
s = "anagram"
t = "nagaram"
print(sol.isAnagram(s,t))
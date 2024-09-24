class Solution(object):    
    def characterReplacement(self, s, k):
        l = 0
        frequency = {}
        longest = 0
        for r in range(len(s)):    
            if not s[r] in frequency:
                frequency[s[r]] = 0
            frequency[s[r]] += 1 
            count = r - l + 1
            if count - max(frequency.values()) <= k:
                longest = max(longest, count) 
                print("count") 
            else:
                frequency[s[l]] -= 1
                if not frequency[s[l]]:
                    frequency.pop(s[l])
                l += 1
                print("l")
            print(frequency)
        return longest
s = "ABAB"
k = 2
solution = Solution()
print(solution.characterReplacement(s, k))
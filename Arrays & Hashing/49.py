from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        anagram = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            anagram[key].append(str)
        return anagram.values()

sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))
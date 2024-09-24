class Solution(object):
    def minExtraChar(self, s, dictionary):
        char_set = set(''.join(dictionary))
        extra_chars = 0
        for c in s:
            if c not in char_set:
                extra_chars += 1

        return extra_chars

s = "dwmodizxvvbosxxw"
dictionary = ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]
solution = Solution()
print(solution.minExtraChar(s, dictionary))

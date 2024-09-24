from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        n, l = len(s1), len(s2)
        source = Counter(s1)
        window = Counter(s2[:n])
        for i in range (1, l-n+1):
            if source == window:
                return True
            left_char = s2[i - 1]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            
            right_char = s2[i + n - 1]
            window[right_char] += 1
        if source == window:
            return True
        else:
            return False

s1 = "adc"
s2 = "dcda"
solution = Solution()
print(solution.checkInclusion(s1, s2))
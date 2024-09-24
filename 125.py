import string
class Solution(object):
    def isPalindrome(self, s):
        remove_chars = string.punctuation + " "
        s = ''.join(char.lower() for char in s if char.isalnum())
        n = len(s)//2
        print(n, len(s))
        for i in range (n):
            j = len(s)-i-1
            if s[i] == s[j]:
                continue
            else:
                return False
        return True

solution = Solution()
s = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s))
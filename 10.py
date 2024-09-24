class Solution(object):
    def isMatch(self, s, p):
        n = len(p)
        l = len(s)
        dp = [0]*(n-l+1)
        for j in range (n-l+1):
            substring = p[j:j+l]
            for i in range(l):
                if substring[i] == '.':
                    continue
                elif substring[i] == '*':
                    if (i > 0 and s[i] == substring[i-1]) or substring[i-1] == '.':
                        continue
                    else:
                        break
                elif not s[i] == substring[i]:
                    break
        return False
    
s = "aab"
p = "c*a*b"
solution = Solution()
print(solution.isMatch(s, p))
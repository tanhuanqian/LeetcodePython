class Solution(object):
    def myAtoi(self, s):
        negative = False
        nums = 0
        flag = False
        n = len(s)
        for i in range(0,n):
            if not flag and s[i] == ' ':
                continue
            elif not flag and (s[i] == '+' or s[i] == '-'):
                flag = True
                if s[i] == '-':
                    negative = True
            elif '0' <= s[i] <= '9':
                flag = True
                nums = nums*10 + (ord(s[i])-ord('0'))
            else:
                break
        if negative:
            nums = -nums
        return max(-2**31, min(nums, 2**31 - 1))
s = "+-123cd"
solution = Solution()
print(solution.myAtoi(s))
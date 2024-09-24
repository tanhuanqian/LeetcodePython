class Solution(object):
    def reverse(self, x):
        y = 0
        negative = x < 0
        x = abs(x)
        while x > 0:
            y = y * 10 + (x%10)
            x //= 10
        if negative:
            y = -y
        if y > 2**31 - 1 or y < -2**31:
            return 0
        return(y)
x = 123
solution = Solution()
print(solution.reverse(x))
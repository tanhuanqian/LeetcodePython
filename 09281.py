class Solution(object):
    def minElement(self, nums):
        res = []
        for num in nums:
            sum = 0
            while num >= 10:
                sum += num%10
                num /= 10
            sum += num
            res.append(int(sum))
        return min(res)

sol = Solution()
nums = [10,12,13,14]
print(sol.minElement(nums))
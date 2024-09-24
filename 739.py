class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        daily = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(stack) > 0:
                print(stack)
                if temperatures[i] > temperatures[stack[-1]]:
                    daily[stack[-1]] = i-stack[-1]
                    stack.pop()
                else:
                    break
            stack.append(i)
        return daily

nums = [73,74,75,71,69,72,76,73]
solution = Solution()
print(solution.dailyTemperatures(nums))
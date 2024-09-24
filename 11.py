class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height)-1
        maxarea = 0
        while i < j:
            area = min(height[i], height[j]) * (j-i)
            maxarea = max(area, maxarea)
            print(height[i], height[j])
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return maxarea
    
height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
print(solution.maxArea(height))
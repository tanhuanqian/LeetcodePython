from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        top = count.most_common(k)
        top_elements = [element for element, _ in top]
        return top[0][0]
    
nums = [1,1,1,2,2,3]
k = 2
solution = Solution()
print(solution.topKFrequent(nums,k))
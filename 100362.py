import heapq
class Solution(object):
    def resultsArray(self, queries, k):
        result = []
        heap = []
        for query in queries:
            x, y = query
            distance = abs(x)+abs(y)
            heapq.heappush(heap, -distance)
            if len(heap) > k:
                heapq.heappop(heap)
            if len(heap) < k:
                result.append(-1)
            else:
                result.append(-heap[0])
        return result
    
queries = [[1,2],[3,4],[2,3],[-3,0]]
k = 2
solution = Solution()
print(solution.resultsArray(queries, k))
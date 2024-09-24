class Solution(object):
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0])
        front = 0
        end = row*col-1
        while front <= end:
            mid = (front+end)//2
            a = mid//col
            b = mid%col
            print(matrix[a][b], mid, a, b)
            if matrix[a][b] < target:
                front = mid+1
            elif matrix[a][b] > target:
                end = mid-1
            else:
                return True
        return False
        
matrix = [[1,3]]
target = 3
solution = Solution()
print(solution.searchMatrix(matrix, target))
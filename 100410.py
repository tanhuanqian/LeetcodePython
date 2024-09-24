class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        color1 = (ord(coordinate1[0]) - ord('a') + int(coordinate1[1])) % 2
        color2 = (ord(coordinate2[0]) - ord('a') + int(coordinate2[1])) % 2
        return color1 == color2

coordinate1 = "a1"
coordinate2 = "c3"
solution = Solution()
print(solution.checkTwoChessboards(coordinate1, coordinate2))
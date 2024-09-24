import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        minspeed = 1
        maxspeed = max(piles)
        while minspeed <= maxspeed:
            speed = minspeed + (maxspeed-minspeed) // 2
            totaltime = 0
            for pile in piles:
                totaltime += (pile//speed)
                if pile%speed != 0:
                    totaltime += 1
            if totaltime <= h:
                maxspeed = speed-1
            else:
                minspeed = speed+1
        return minspeed

piles = [312884470]
h = 312884469
solution = Solution()
print(solution.minEatingSpeed(piles, h))
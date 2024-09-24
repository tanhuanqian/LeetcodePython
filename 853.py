class Solution(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        for p, s in cars:
            time = int((target - p) / float(s))
            if not stack or time > stack[-1]:
                stack.append(time)
                
        return len(stack)
    
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
solution = Solution()
print(solution.carFleet(target, position, speed))
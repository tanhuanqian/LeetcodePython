class Solution(object):
    def trap(self, height):
        ans = 0
        left = 0
        right = len(height)-1
        pre_max = 0
        suf_max = 0
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max <= suf_max:
                ans += pre_max-height[left]
                print("left", pre_max, height[left], left)
                left += 1
            else:
                ans += suf_max - height[right]
                print("right", suf_max, height[right], right)
                right -= 1
            print(ans)
        return ans


nums = [0,1,0,2,1,0,1,3,2,1,2,1]
solution = Solution()
print(solution.trap(nums))
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        total_len = len(nums1) + len(nums2)
        half = (total_len + 1) // 2
        start, end = 0, len(nums1)
        
        while start <= end:
            mid1 = (start + end) // 2
            mid2 = half - mid1
            
            left1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            left2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            right1 = nums1[mid1] if mid1 < len(nums1) else float('inf')
            right2 = nums2[mid2] if mid2 < len(nums2) else float('inf')
            
            if left1 <= right2 and left2 <= right1:
                if total_len % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                else:
                    return max(left1, left2)
            elif left1 > right2:
                end = mid1 - 1
            else:
                start = mid1 + 1


nums1 = [1,2]
nums2 = [3,4]
solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))
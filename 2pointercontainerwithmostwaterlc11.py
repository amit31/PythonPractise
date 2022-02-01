from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        maxarea = 0

        while left <= right:
            area = (right - left) * min(height[right], height[left])
            maxarea = max(maxarea, area)
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        return maxarea

s=Solution()

ans=s.maxArea([1,8,6,2,5,4,8,3,7])
print(ans)
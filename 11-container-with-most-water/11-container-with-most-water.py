class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
       
        maxarea=0
        
        while left<=right:
            area=(right-left)*min(height[right],height[left])
            maxarea = max(maxarea,area)
            if height[left] < height[right]:
                left=left+1
            else:
                right=right-1
        
        return maxarea
        
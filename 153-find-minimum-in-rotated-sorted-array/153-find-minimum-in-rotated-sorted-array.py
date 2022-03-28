class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        mine = min(nums)
        
        
        for i in nums:
            if mine==i:
                return mine
        
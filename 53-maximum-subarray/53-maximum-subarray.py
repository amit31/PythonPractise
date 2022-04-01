class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        suma=nums[0]
        sumb=0
        n=len(nums)
        if n==1:
            return nums[0]
        for i in range(len(nums)):
            if(sumb < 0):
                sumb = 0
            sumb=sumb+nums[i] 
            suma=max(suma,sumb)
                
        return suma
            
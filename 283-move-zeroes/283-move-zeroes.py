class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size=len(nums)
        j=0
        for i in range(size):
             if nums[i]!=0:
              nums[j]=nums[i]
              j=j+1
        while j <size:
         nums[j]=0
         j=j+1
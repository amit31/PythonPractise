class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        count=0
        for i in range(1,len(nums)):
            
            if nums[i]!=nums[i-1]:
                count=0
                nums[k]=nums[i]
                k=k+1
            elif count<1:
                
                count=count+1
                
                
                nums[k]=nums[i]
                k=k+1
                
                
        return k
            
                
    
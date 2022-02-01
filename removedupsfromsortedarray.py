from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[k]=nums[i+1]
                k=k+1
        return k
s=Solution()

ans=s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(ans)

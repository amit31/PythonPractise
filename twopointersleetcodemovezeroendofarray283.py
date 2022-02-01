from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        size=len(nums)
        j=0

        for i in range(size):
            if nums[i]!=0:
                nums[j]=nums[i]
                j=j+1
        while j <size:
                nums[j]=0
                j=j+1
        return nums

s=Solution()
ans=s.moveZeroes([0,2,0,1])
print(ans)

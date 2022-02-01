from typing import List


class Solution:
    def firstOccurance(self,s:List[int],target) -> int:

        left = 0
        right = len(s)-1
        while (left <= right):
         mid=int((left+right)/2)
         if s[mid]==target :
            if s[mid-1] !=target and mid ==0:
                return mid
            right=(mid-1)
         elif s[mid]>target:
            right=mid-1
         else:
            left=mid+1
        return mid





    def lastOccurance(self,s:List[int],target) -> int:

        left = 0
        right = len(s)-1
        while (left <= right):
            mid=int((left+right)/2)
            if s[mid]==target :
                if s[mid+1] !=target  and mid+1 <len(s) or mid ==len(s)-1:
                    return mid
                left=mid+1
            elif s[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return mid

    def getRightPosition(self,nums,target):

        left=0
        right=len(nums)-1

        while (left<=right):
            mid=(left+right)/2

            if nums[mid]==target:
             if mid+1 <len(nums) and nums[mid+1]!=target or mid ==len(nums)-1:
                 return mid
             left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1


s=Solution()
answer=s.firstOccurance([1,1,2,3,4],1)
ab=s.lastOccurance([1,1,2,3,4],1)
print(ab)

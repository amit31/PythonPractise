class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        big=len(nums)-1
        small=0
        
        
        
        while small<= big:
              mid=(small+big)//2
              if nums[mid] == target:
                    return mid
              elif nums[mid] < target:
                     small=mid+1
              elif nums[mid] > target:
                    big=mid-1
              
        return -1
    
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low=0
        high=len(nums)-1
        nums1=sorted(nums)
        print(nums1)
        k=0
        while low <=high:
            mid=(low+high)//2
            if nums1[mid] == target:
                k=nums1[mid]
                return nums.index(k)
            elif target < nums1[mid]:
                 high = mid -1
            elif target > nums1[mid]:
                 low = mid + 1
            
        return -1
     
            
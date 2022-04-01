class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a=[]
        b=[]
        for i in set(nums1):
            print(i)
            if i not in nums2:
                a.append(i)
        for i in set(nums2):
            print(i)
            if i not in nums1:
                b.append(i)
        return [a,b]
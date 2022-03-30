class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        i=0
        j=0
        mergedarray=[]
        
        while i <len(nums1) and j <len(nums2):
            if nums1[i] >nums2[j]:
                mergedarray.append(nums2[j])
                j=j+1
            else:
                mergedarray.append(nums1[i])
                i=i+1
           
        while j<len(nums2):
                mergedarray.append(nums2[j])
                j=j+1
        while i<len(nums1):
                mergedarray.append(nums1[i])
                i=i+1
        
        
        if len(mergedarray)%2 !=0:
            median = float(mergedarray[len(mergedarray)//2])
        
        if len(mergedarray)%2 ==0:
            print(mergedarray[len(mergedarray)//2]-1)
            median = float(( mergedarray[len(mergedarray)//2-1]+mergedarray[(len(mergedarray)//2)])/2)
        
        return median
            
        
            
        
      
        
        
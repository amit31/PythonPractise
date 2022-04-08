class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
        len1=len(nums1)
        len2=len(nums2)
        # if len2 > len1:
        #     nums1,nums2=nums2,nums1
        m={}
        k=[]
        j=0
        for i in nums1:
            m[i]=m.get(i,0)+1
        print(m)
        
        for key,value in m.items():
            j=0
            while j < len(nums2):
                if nums2[j] == key and value>=1:
                    k.append(nums2[j])
                    value=value-1
                    j=j+1
                else:
                    j=j+1
                
        return k
        
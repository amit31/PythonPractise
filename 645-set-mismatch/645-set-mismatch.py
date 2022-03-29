class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen=set(nums)
        
        m={}
        dup=0
        missingnums=0
        size=len(nums)
        
        for i in nums:
            m[i]=m.get(i,0)+1
        
        for key,value in m.items():
            if value==2:
                dup = key
        
        
        for i in range(1,len(nums)):
            
            if i not in seen:
                missingnums = i
                break
        print(missingnums)
        if missingnums==0:
            missingnums=len(nums)
        
        return[dup,missingnums]
                
            
            
            
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen={}
        dup=0
        missingnums=0
        size=len(nums)
        for i in nums:
            seen[i]=seen.get(i,0)+1
        print(seen)
        
        for key,value in seen.items():
            if value==2:
                dup = key
        for i in range(1,len(nums)):
            print(i)
            if i in nums:
                pass
            else:
                missingnums=i
                break
        if missingnums==0:
            missingnums=size
                
                
        return[dup,missingnums]
            
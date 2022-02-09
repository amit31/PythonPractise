class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count=0
        nums=sorted(nums)
        #nums=list(set(nums))
      
                    
            
        
        
        j=1
        m={}
        for i in nums:
            m[i]=m.get(i,0)+1
        print(m)
        for i in m:
            print(i)
            goal =k+i
            if goal in m and k!=0:
                count=count+1
            elif k==0:
                 if(m[i]>=2):
                    count=count+1
        return count
        
        
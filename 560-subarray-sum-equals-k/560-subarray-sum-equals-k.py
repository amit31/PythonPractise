class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        
        m={0:1}
        summ=0
        for i in nums:
            summ=summ+i
            #prefix sum concept 
            if summ-k in m:
                count=count+m.get(summ-k)
                
            m[summ]=m.get(summ,0)+1
            
       
        return count
            
        
            
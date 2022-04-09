class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        sorted_l=[]
        m={}
        j=0
        for i in nums:
            m[i]=m.get(i,0)+1
        
        m=(sorted(m.items(), key =
             lambda kv:(kv[1]),reverse=True)) 
        print(m)  
        while j<k:
            sorted_l.append(m[j][0])
            j=j+1
            
        return sorted_l
            
           
                
            
        
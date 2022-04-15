class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        j=[]
        m={}
        k={}
        ans=""
            
        k=0
        for i in indices:
            m[i]=s[k]
            
            k=k+1
        
        
        
        
        k=sorted(m.items(),key=lambda x:x[0])
        
        
        
        for i in k:
            j.append(i[1])
        
        return ans.join(j)
        
            
            
            
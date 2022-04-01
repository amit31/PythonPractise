class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
      
        k=[]
        for i in range(len(s)-1,-1,-1):
            k.append(s[i])
    
        j=len(k)
        
        for j in range(0,len(k),1):
            print(k[j])
            s[i]=k[j]
            i=i+1
    
       
       
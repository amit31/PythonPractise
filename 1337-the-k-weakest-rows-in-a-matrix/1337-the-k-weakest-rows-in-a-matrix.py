class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        mapm={}
        sortedm=[]
        s=[]
        for i in range(len(mat)):
            row=0
            count=0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    count=count+1
            mapm[i]=count
        
        
         
        s=sorted(mapm.items(), key=lambda x: (x[1],x[0]))
       
        y=[x[0] for x in s]
        print(y)
        
        return y[:k]
   
    
                 
           
        
      
            
        
            
        
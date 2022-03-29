class Solution:
    
    def combination(self,candidates,target,ans,cur,add,index):
        if add==target:
            ans.append(cur[:])
        elif add<target:
            for i in range(index,len(candidates)):
           
                cur.append(candidates[i])
                self.combination(candidates,target,ans,cur,add+candidates[i],i)
                cur.pop()
            return
   
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans=[]
        cur=[]
        add=0
        self.combination(candidates,target,ans,cur,add,0)
       
        return ans
        
        
        
        
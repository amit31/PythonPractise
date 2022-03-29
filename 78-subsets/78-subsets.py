class Solution:
    
    def makesubsets(self,nums:List[int],ans:List[int],cur:List[int],index):
        if index >= len(nums):
            return
        ans.append(cur[:])
        for i in range(index,len(nums)):
            if nums[i] not in cur:
                cur.append(nums[i])
                self.makesubsets(nums,ans,cur,i)
                cur.pop()
        
        return
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur=[]
        ans=[]
        self.makesubsets(nums,ans,cur,0)
        return ans
        
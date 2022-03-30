
"""
def makesubsets(nums[],cur[],ans[],i)

base case if index > len(nums):
             return
      ans.append(cur[:])
      algo: 
      loop from i to len(nums)
        if nums[i] not in cur
         cur.append(nums[i])-->take case
         makesubsets(nums,cur,ans,i)
         cur.pop()-->remove case

Always the pattern is :

123
1 3
12
 23
  3
 2
1
none selected

 number of subsets is 2^n as choice is 2 for all inputs(n)

"""


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
        
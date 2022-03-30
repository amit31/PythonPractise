class Solution:
    
     def makesubsets(self, nums: List[int], cur: List[int], ans: List[int], index, target):
        if index == len(nums):

            if target == 0:
                ans.append(cur[:])
            return

        if nums[index] <= target:
            cur.append(nums[index])
            self.makesubsets(nums, cur, ans, index , target - nums[index])
            cur.remove(nums[index])
        self.makesubsets(nums, cur, ans, index + 1, target)
   
     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        cur = []
        ans = []
        self.makesubsets(candidates, cur, ans, 0, target)
        return ans
        
        
        
        
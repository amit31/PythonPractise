from typing import List


class Solution:
    def solution(self, nums, ans, cur, index):

        if (index > len(nums)): #([],[1[,[1,2])
            return
        ans.append(cur[:])
        for i in range(index, len(nums)):
            if nums[i] not in cur:                #
                cur.append(nums[i])               #nums,ans,[1,2],1
                self.solution(nums, ans, cur, i)  # nums,ans,[1],0
                cur.pop()
        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        self.solution(nums, ans, cur, 0)
        return ans

s = Solution()
ans=s.subsets([1,2])
print(ans)


from typing import List


class Solution:

    def add(self, ans, cur, candidates, target, index, sum):

        if sum == target:
            ans.append(cur[:])
        elif sum < target:
            n = len(candidates)
            for i in range(index, n):
                cur.append(candidates[i])
                self.add(ans, cur, candidates, target, i, sum + candidates[i])
                cur.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        cur = []
        self.add(ans, cur, candidates, target, 0, 0)

        return ans

s=Solution()
ans=s.combinationSum([2,3,6,7],7)
print(ans)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum_a=0
        maxs=0
        for i in gain:
            sum_a=sum_a+i
            maxs=max(maxs,sum_a)
        return maxs
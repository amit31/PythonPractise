class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
       x= [num*num for num in nums]
       y=sorted(x)
       return y
       
       
        
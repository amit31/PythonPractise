class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size=len(digits)
        s = [str(i) for i in digits]
        numbers = "".join(s)
        
        numbers=int(numbers)+1
        
        
        y=[x for x in str(numbers)]
        return y
        
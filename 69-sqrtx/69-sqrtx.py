class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        h=x
        
        while l<=h:
            m=l+(h-l)//2
            
            if m*m == x:
                return m
            
            if m*m > x:
                h=m-1
            else:
                l=m+1
        return h
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s=[s for s in s]
        t=[t for t in t ]
        
        s=sorted(s)
        print(s)
        t=sorted(t)
        print(t)
        
        if s ==t:
            return True
        else:
            return False
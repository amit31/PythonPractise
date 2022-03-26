class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # s= [str(x) for x in  s]
        # t= [str(x) for x in  t]
        j=0
        k=0
        l=0
        while j <len(s) and k < len(t):
            if s[j]==t[k]:
                j=j+1
                k=k+1
            else:
                k=k+1
            
        return j == len(s)
            
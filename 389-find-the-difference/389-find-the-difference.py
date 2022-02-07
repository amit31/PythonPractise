class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        m={}
        k={}
        s=sorted(s)
        t=sorted(t)
        for i in s:
            m[i]=m.get(i,0)+1
        for i in t:
            k[i]=k.get(i,0)+1
        print(k)
        for i in (t):
            if(m.get(i))!=k.get((i)):
                return i
            
            
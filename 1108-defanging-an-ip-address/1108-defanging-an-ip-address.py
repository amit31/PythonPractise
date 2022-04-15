class Solution:
    def defangIPaddr(self, address: str) -> str:
        s=""
        for i in address:
            if i==".":
                i="[.]"
                s=s+i
            else:
                s=s+i
        return s
            
        
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k=1
        if needle=="":
            return 0
        size=len(haystack)
        sizen=len(needle)
        for i in range(0,len(haystack)):
            
            if haystack[i:i+sizen] == needle:
                return i
        return -1
    
            
            
            
        
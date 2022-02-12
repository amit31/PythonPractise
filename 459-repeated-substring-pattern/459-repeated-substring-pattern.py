class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        lengths=len(s)
        rep=''
        for i in range(0,lengths//2):
            rep=rep+s[i]
            if lengths%len(s)==0:
                if rep*(lengths//len(rep))==s:
                    return True
        return False
        
        
    
            
            
            
          
        
    
    
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
         strp=re.sub('[^A-Za-z0-9]+', '', s)
         strp=strp.lower()
         strp=[strp for strp in strp]
         print(strp)
         
         right=len(strp)-1
         for i in range(0,right):
            if strp[i]!=strp[right]:
                return False
            else:
                right=right-1
         return True
                
        
        
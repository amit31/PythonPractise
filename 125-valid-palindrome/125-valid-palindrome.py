import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
         strp=re.sub('[^A-Za-z0-9]+', '', s)
         strp=strp.lower()
         strp=[strp for strp in strp]
         print(strp)
         left=0
         count=0
         right=len(strp)-1
         for i in range(0,right):
            if strp[i]!=strp[right]:
                print(strp[left])
                print(strp[right])
                count=count+1
                print(count)
                return False
            else:
                right=right-1
         return True
                
        
        
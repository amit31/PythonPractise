class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s=s.strip(" ")
        str_s=s.split(" ")
        print(str_s)
        
        size=len(str_s)
        
        last=size-1
        
        
        
        return len(str_s[last])
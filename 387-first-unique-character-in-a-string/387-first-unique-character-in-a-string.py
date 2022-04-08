class Solution:
    def firstUniqChar(self, s: str) -> int:
        map_m={}
        
        for i in range(len(s)):
            map_m[s[i]]=map_m.get(s[i],0)+1
        
        
        for key,value in map_m.items():
            
            if value==1:
                return s.index(key)
        return -1
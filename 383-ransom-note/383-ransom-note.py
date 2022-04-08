class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        map_r={}
        map_m={}
        ransomNote=[x for x in ransomNote]
        magazine=[y for y in magazine]
        k=0
        for j in magazine:
            map_m[j]=map_m.get(j,0)+1
        print(map_m)
        for k in range(0,len(ransomNote)):
            
              key=ransomNote[k]
              if map_m.get(key,0) >0:
                    print(map_m[key])
                    map_m[key]= map_m[key]-1
                    
              else:
                    return False
            
        return True
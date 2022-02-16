class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        maps={}
        ans=[]
        for i in nums:
            maps[i]=maps.get(i,0)+1
        print(maps)   
            
        for key,value in maps.items():
            if value==1:
                ans.append(key)
        return ans
              
                
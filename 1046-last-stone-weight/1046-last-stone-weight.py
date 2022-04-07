class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones=sorted(stones)
        
        
        big=len(stones)-1
        
        
        
        while big >=1:
            if stones[big] >stones[big-1]:
                stones[big-1]=stones[big]-stones[big-1]
                stones.remove(stones[big])
                big=big-1
                stones=sorted(stones)
            elif stones[big] ==stones[big-1]:
                    stones.remove(stones[big])
                    stones.remove(stones[big-1])
                    stones=sorted(stones)  
                    big=big-2
        if len(stones):
            return stones[0]
        else :
            return 0
   
        
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        count=1
        arr=sorted(arr)
        diff=arr[1]-arr[0]
        for i in range(len(arr)-1):
            if arr[i]+diff==arr[i+1]:
                count=count+1
        if count==len(arr):
            return True
        else:
            return False
            
        
        
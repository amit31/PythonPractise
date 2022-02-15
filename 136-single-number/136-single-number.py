class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
#         size=len(nums)
        
#         a=[]
        
#         for i in nums:
#             if i not in a:
#              a.append(i)
            
         
#         totals=sum(a)*2
#         result = totals-totald
        
#         return result
        
         
         
         return 2*sum(set(nums)) - sum(nums)
         
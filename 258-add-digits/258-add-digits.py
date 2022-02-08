class Solution:
    def addDigits(self, num: int) -> int:
        
        
       
        zk=len(str(num))
        while zk>=1:
            
            nums=[int(x) for x in str(num)]
            print(nums)
            z=sum(nums)
            num=z
            zk=zk-1
        return z
        
           
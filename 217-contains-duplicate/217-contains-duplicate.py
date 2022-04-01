class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count=0
        size=len(nums)
        if size==1:
            return False
        m_dict={}
        
        for i in range(0,int(len(nums))):
            m_dict[nums[i]]=m_dict.get(nums[i],0)+1
            
        print(m_dict)
        for value in m_dict.values():
            print(value)
            if value > 1:
                return True
        return False
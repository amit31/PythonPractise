# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ans = ListNode(0)
        ans.next=head
        
        slow=ans
        fast=ans
        med=ans
        
        for i in range(1,k+1):
            
            med=med.next
            fast=fast.next
        
        while fast is not None:
            fast=fast.next
            slow=slow.next
        
        
        med.val,slow.val=slow.val,med.val
        
        return ans.next
        
            
            
        
        
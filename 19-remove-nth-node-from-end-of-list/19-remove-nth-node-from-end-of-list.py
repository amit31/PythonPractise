# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ans = ListNode(0)
        ans.next=head
        
        fast=ans
        slow=ans
        
        for i in range(1,n+2):
            fast=fast.next
        
        
        while fast is not None:
            slow=slow.next
            fast=fast.next
           
        
        slow.next=slow.next.next
        
        return ans.next
    
        
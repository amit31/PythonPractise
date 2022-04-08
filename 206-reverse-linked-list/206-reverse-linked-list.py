# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        helper = None
        while head is not None:
            next=head.next
            head.next=helper
            helper=head
            head = next
        return helper
        
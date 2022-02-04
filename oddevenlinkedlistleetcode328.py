# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head) -> [ListNode]:
        if not head:
            return head
        odd=head
        even=odd.next
        evenlist=even

        while even and even.next:
            odd.next=even.next
            odd=odd.next

            even.next=odd.next
            even=even.next

        odd.next=evenlist
        return head

s=Solution()

node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)
node4=ListNode(4)
node5=ListNode(5)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

ans=s.oddEvenList(node1)

while ans is not None:
    print(ans.val)
    ans=ans.next
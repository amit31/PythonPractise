# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:

        ans = ListNode(0)
        ans.next = head

        fast = ans
        slow = ans

        for i in range(1, n + 2):
            if fast.next == None:
                return "Check the node again"
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return ans.next



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

ans=s.removeNthFromEnd(node1,3)
print (ans)
while ans is not None:
    print(ans.val)
    ans=ans.next
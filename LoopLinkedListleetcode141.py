# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: [ListNode]) -> bool:
        fast = head
        slow = head

        while fast and slow and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False

s = Solution()
node1 = ListNode(1)
node5 = ListNode(5)
node11= ListNode(11)
node8= ListNode(8)
node9= ListNode(9)

node1.next=node5
node5.next=node11
node11.next=node8
node8.next=node9
#node9.next=node5

ans= s.hasCycle(node1)
print(ans)







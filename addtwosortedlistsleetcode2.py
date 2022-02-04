# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        sum=0
        carry=0
        ans = ListNode(None)
        pointer = ans

        while l1 or l2 is not None:
            sum=carry
            if l1 != None:
              sum=sum+l1.val
              l1=l1.next

            if l2 != None:
                 sum = sum + l2.val
                 l2 = l2.next

            carry = int(sum/10)
            pointer.next=ListNode(sum%10)
            pointer=pointer.next


        if carry >0:
            pointer.next = ListNode(carry)
        return ans.next



s=Solution()
l1_n1=ListNode(2)
l1_n2=ListNode(4)
l1_n3=ListNode(3)

l1_n1.next=l1_n2
l1_n2.next=l1_n3

# 342
# 465
# -------
# 807
l2_n1=ListNode(5)
l2_n2=ListNode(6)
l2_n3=ListNode(4)

l2_n1.next=l2_n2
l2_n2.next=l2_n3

ans=s.addTwoNumbers(l1_n1,l2_n1)
while ans is not None:
    print(ans.val)
    ans=ans.next

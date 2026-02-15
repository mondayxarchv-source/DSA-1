# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def midNode(self, head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def reverseList(self, head):
        pre=None
        cur=head
        while cur:
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
        return pre

    def pairSum(self, head):
        mid=self.midNode(head)
        head2=self.reverseList(mid)
        maximum=0
        while head2:
            total=head.val+head2.val
            if total>maximum:
                maximum=total
            head=head.next
            head2=head2.next
        return maximum
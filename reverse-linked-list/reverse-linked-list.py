# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None: return head
        if head.next is None: return head
        old_next = head.next
        new_next=None
        head.next = new_next
        prev = head
        head = old_next
        while head.next is not None:
            
            new_next=prev
            old_next = head.next
            head.next = new_next
            prev =head
            head = old_next

#         new_next = head
#         next = head.next
#         head.next = new_next
#         head= next
        head.next = prev
        return head
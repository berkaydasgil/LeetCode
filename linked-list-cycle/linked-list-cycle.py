# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        setA = set()
        
        while head is not None:
            if head in setA:
                return head
            setA.add(head)
            head=head.next
            
            
        
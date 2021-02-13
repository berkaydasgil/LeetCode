# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head: ListNode)->ListNode:
        node = head
        tmp = None
        while node is not None:
            nextp = node.next
            node.next = tmp
            tmp = node
            node= nextp
        return tmp
    
    def isPalindrome(self, head: ListNode) -> bool:

                
        if head is None: return True
        if head.next is None: return True

        fast = head
        slow = head
        
        while fast.next is not None and fast.next.next is not None:
            fast=fast.next.next
            slow=slow.next
        
        firsthalf = head
        secondhalf = self.reverse(slow.next)
        # print(firsthalf,secondhalf,sep=' ||||',end='\n\n')

        while secondhalf and firsthalf :
            if secondhalf.val == firsthalf.val:
                firsthalf= firsthalf.next
                secondhalf= secondhalf.next
                # print(firsthalf,secondhalf,sep=' ||||',end='\n\n')
            else: 
                # print('final', firsthalf, secondhalf,sep=' ||||',end='\n\n')
                return False
        return True



        
        
        
        

        
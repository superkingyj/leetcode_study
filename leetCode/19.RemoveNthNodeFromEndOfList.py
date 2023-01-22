from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # TC --> O(N^2)
        # SC --> O(1)
        
        p = ListNode(None, None)
        p.next = head
        
        while True: 
            check = p 
            
            for _ in range(n+1):            
                check = check.next
                
            if check == None:
                if p.next == head: # [1] 1 / [1,2] 2
                    p.next = p.next.next
                    head = p.next
                    break
                p.next = p.next.next
                break
                
            p = p.next
            
        return head 


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        
        for _ in range(n):
            fast = fast.next
        
        if not fast:
            return slow.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #TC --> O(N)
        #SP --> O(N)
        
        p1 = list1
        p2 = list2
        p = ListNode() # val = 0, next = None

        if p1 == None:
            return p2
        if p2 == None:
            return p1
        
        prev = p
        head = p
        
        while True:
            if p1 == None:
                p.val = p2.val 
                p.next = p2.next
                break  
            elif p2 == None:
                p.val = p1.val
                p.next = p1.next
                break 
            
            if p1.val < p2.val:
                p.val = p1.val
                prev = p
                p = ListNode()
                prev.next = p
                p1 = p1.next
            else:
                p.val = p2.val
                prev = p
                p = ListNode()
                prev.next = p
                p2 = p2.next
                
        return head
                

                
        
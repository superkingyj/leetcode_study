from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        s = set()
        p = head
        
        while True:
            if not p: return False
            
            if p in s: return True
            else: s.add(p)
            
            p = p.next
    
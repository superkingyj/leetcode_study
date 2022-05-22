from queue import PriorityQueue
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        q = PriorityQueue()
        dummy = ListNode()
        p = dummy
        
        for idx, node in enumerate(lists):
            if node: q.put((node.val, idx, node))
                
        while True:
            if q.qsize() <= 0:
                break
            _, idx, p.next = q.get()
            p = p.next
            if p.next: q.put((p.next.val, idx, p.next))
            
        return dummy.next
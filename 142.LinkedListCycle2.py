# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        check, p, flag = set(), head, False
        
        while p: 
            if p in check:
                flag = True
                break
            check.add(p)
            p = p.next
            
        if flag: return p    
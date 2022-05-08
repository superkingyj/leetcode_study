# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2, i,j = 0, 0, 0, 0
        node = l1
        while True:
            temp = (node.val)*(pow(10,i))
            num1 += temp
            if node.next:
                node = node.next
                i += 1
            else:
                break
        
        node = l2
        while True:
            temp = (node.val)*(pow(10,j))
            num2 += temp
            if node.next:
                node = node.next
                j += 1
            else:
                break
        
        num = num1 + num2
        num = str(num)

        char = ListNode()
        char_head = char
        i = len(num)-1

        while True:
            char.val = int(num[i])
            new_char = ListNode()
            
            if i > 0:
                char.next = new_char
                char = new_char
                i -= 1
            else:
                break
        
        return char_head


sol = Solution()
print(sol.addTwoNumbers([2,4,3], [5,6,4]))

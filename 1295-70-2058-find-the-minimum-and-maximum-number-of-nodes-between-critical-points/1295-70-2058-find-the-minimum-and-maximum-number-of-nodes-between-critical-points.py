# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr = head
        prev_val = curr.val
        latest_index = -1
        min_index = float(inf)
        min_dist, max_dist = float(inf), -1
        cnt = 0
        index = 1

        def is_critical(prev_val, curr_val, next_val):
            if (curr_val < prev_val and curr_val < next_val):
                return True
            if (curr_val > prev_val and curr_val > next_val):
                return True
            return False
        
        while curr.next:
            if is_critical(prev_val, curr.val, curr.next.val):
                # print(index, curr.val)
                cnt += 1
                min_index = min(min_index, index)
                max_dist = index-min_index
                if latest_index < 0:
                    latest_index = index
                else:
                    min_dist = min(min_dist, index-latest_index)
                latest_index = index
            
            prev_val = curr.val
            curr = curr.next
            index += 1

        if cnt < 2: return [-1, -1]
        return [min_dist, max_dist]
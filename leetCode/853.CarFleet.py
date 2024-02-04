class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_n_speed_n_dest = [(p, s, (target-p)/s) for p, s in zip(position, speed)]
        pos_n_speed_n_dest.sort(key = lambda x:(-x[0], -x[1]))

        stack = []
        for p, s, d in pos_n_speed_n_dest:
            stack.append(d)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
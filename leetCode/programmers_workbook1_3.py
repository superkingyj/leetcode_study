from collections import deque

def solution(order):
    answer = 0
    n, order, sub_s, num = len(order), deque(order), [], 1

    while order and num <= n + 1:
        if sub_s and sub_s[-1] == order[0]:
            sub_s.pop()
            order.popleft()
            answer += 1
            continue
        
        if num == order[0]:
            order.popleft()
            answer += 1
        else:
            sub_s.append(num)

        num +=1
            
    return answer

print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))
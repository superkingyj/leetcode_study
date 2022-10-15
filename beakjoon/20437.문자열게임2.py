import sys

def count_char():
    for c in W:
        char_cnt[ord(c)%97] += 1  

def get_min_max_string():
    global min_cnt, max_cnt
    for i in range(l):
        c = W[i]
        if char_cnt[ord(c)%97] < K: continue

        cnt = 0
        for j in range(i, l):
            if c == W[j]:
                cnt += 1
            if cnt == K:
                min_cnt = min(min_cnt, j-i+1)
                max_cnt = max(max_cnt, j-i+1)
                break

T = int(sys.stdin.readline())
for _ in range(T):
    W = sys.stdin.readline().rstrip()
    K = int(sys.stdin.readline())
    l = len(W)
    char_cnt = [0] * 26
    min_cnt = sys.maxsize
    max_cnt = 0
    count_char()
    get_min_max_string()
    if min_cnt == sys.maxsize or max_cnt == 0:
        print(-1)
    else: 
        print(min_cnt, max_cnt)


"""
- W
- K
- l = len(W)
- min_string = sys.maxsize
- max_string = 0
- def find_shortest() <- 3번
    left, right = 0, 0
    char_dict = defaultdict(int)
    while right < l:
        char_dict[W[right]] += 1
        if char_dict[W[right]] == K:
            while char_dict[W[right]] == K:
                char_dict[W[left]] -= 1
                left += 1
            min_string = min(min_string, right - left + 2)
        else:
            right += 1

- def find_longest() <- 4번
    left, right = 0, 0
    char_dict = defaultdict(int)
    while right < l:
        char_dict[W[right]] += 1
        if char_dict[W[right]] == K:
            while char_dict[W[right]] == K and W[left] != char_dict[W[right:
                char_dict[W[left]] -= 1
                left += 1
            max_stirng = max(max_string, right - left + 2)
        else:
            right += 1


"""

"""
0 1 2 3 4 5 6 7 8 9 101112131415
s u p e r a q u a t o r n a d o

0 1 2 3 4 5 6 7 8 9 10111213141516
s u p e r a q u a t o r n a d o u

0 1 2 3 4 5 6
a b a a a b a

"""
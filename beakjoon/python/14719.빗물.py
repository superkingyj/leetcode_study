import sys

H, W = map(int, sys.stdin.readline().split())
water = list(map(int, sys.stdin.readline().split()))

left, right = 0, W-1
l_max, r_max = water[0], water[W-1]
result = 0

while left < right:
    l_max = max(l_max, water[left])
    r_max = max(r_max, water[right])

    if l_max <= r_max:
        result += l_max - water[left]
        left += 1
    else:
        result += r_max - water[right]
        right -= 1

print(result)
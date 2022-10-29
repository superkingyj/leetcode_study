import sys

result = ""

def check(l1, l2, l3):
    if l1 >= l2 and l1 >= l3:
        return l1, l2+l3
    elif l2 >= l1 and l2 >= l3:
        return l2, l1+l3
    elif l3 >= l1 and l3 >= l1:
        return l3, l1+l2

while True:
    l1, l2, l3 = map(int, sys.stdin.readline().split())
    if l1 == l2 == l3 == 0: break

    if l1 == l2 == l3: 
        result += "Equilateral\n"
    elif (l1 == l2 != l3) or(l1 == l3 != l2) or (l2 == l3 != l1):
        max, sum = check(l1, l2, l3)
        if max < sum: result += "Isosceles\n"
        else: result += "Invalid\n"
    elif l1 != l2 != l3:
        max, sum = check(l1, l2, l3)
        if max < sum: result += "Scalene\n"
        else: result += "Invalid\n"

print(result[:-1])
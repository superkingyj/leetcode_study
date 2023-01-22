import sys

A, B = map(int, sys.stdin.readline().split())
prefix = [0] * 60 # 10^16 < 2^60

for i in range(1,60):
    prefix[i] = 2 * prefix[i-1] + 2**(i-1)

def sum_f(num):
    count = 0
    bin_num = bin(num)[2:]
    length = len(bin_num)

    for i in range(length):
        if bin_num[i] == "1":
            pow = length-i-1
            count += prefix[pow]
            count += (num - 2**pow+1)
            num = num - 2 ** pow

    return count

print(sum_f(B) - sum_f(A-1))

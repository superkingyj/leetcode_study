import sys

n = int(sys.stdin.readline())

mapper = {
    0: "CY",
    1: "SK"
}

print(mapper[n%2])

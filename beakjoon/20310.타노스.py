import sys

S = list(sys.stdin.readline().rstrip())

idxs0, idxs1 = [], []
for i in range(len(S)):
    if S[i] == '0': idxs0.append(i)
    else: idxs1.append(i)

for i in range(len(idxs0)-1, (len(idxs0)//2)-1, -1):
    S[idxs0[i]] = ""
for i in range(0, len(idxs1)//2):
    S[idxs1[i]] = ""

print("".join(S))
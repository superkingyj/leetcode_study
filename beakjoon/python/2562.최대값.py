num_list = []

for i in range(9):
    num_list.append(input())

ANSWERE = max(num_list)
print(ANSWERE)
print(num_list.index(ANSWERE) + 1)

import sys

document = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()
l = len(word)
result = 0
idx = len(document)

while idx-l >= 0:
    if document[idx-l:idx] == word: 
        print(f"result: {result}, range: {idx-l}~{idx} {document[idx-l:idx]}")
        result += 1
        idx = idx-l
    else:
        idx -= 1

print(result)
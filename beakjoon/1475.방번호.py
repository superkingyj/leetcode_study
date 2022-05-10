import sys
from collections import Counter
n = sys.stdin.readline()

cnt = Counter(n)

if cnt["9"] >= cnt["6"]:
    temp = (cnt["9"]-cnt["6"]) // 2
    cnt["6"] = cnt["6"] + temp
    cnt["9"] = cnt["9"] - temp
elif cnt["6"] >= cnt["9"]:
    temp = (cnt["6"]-cnt["9"]) // 2
    cnt["9"] = cnt["9"] + temp
    cnt["6"] = cnt["6"] - temp

print(max(cnt.values()))

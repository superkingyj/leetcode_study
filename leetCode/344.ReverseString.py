from typing import *
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            left, right = i, -(i+1)
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
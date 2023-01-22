class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        for i in range(len(s.split())):
            lst = list(s.split()[i])
            for j in range(len(lst)//2):
                left, right = j, -(j+1)
                lst[left], lst[right] = lst[right], lst[left]
            result += "".join(lst)
            result += " " if i < len(s.split())-1 else ""
        return result
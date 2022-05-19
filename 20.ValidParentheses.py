class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char == "(": stack.append(char)
            elif char == "{": stack.append(char)
            elif char == "[":stack.append(char)
            else:
                if not stack:
                    return False
                elif char == ")":
                    if stack.pop() == "(": continue
                    else: return False
                elif char == "}":
                    if stack.pop() == "{": continue
                    else: return False
                elif char == "]":
                    if stack.pop() == "[": continue
                    else: return False
            
        if len(stack) > 0:
            return False
        return True
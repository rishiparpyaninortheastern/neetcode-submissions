class Solution:
    def isValid(self, s: str) -> bool:
        map={'{':'}','[':']','(':')'}
        stack=[]

    

        for i in s:
            if i in map:
                stack.append(i)
            else:
                if not stack or map[stack.pop()] != i:
                    return False
        return not stack
        
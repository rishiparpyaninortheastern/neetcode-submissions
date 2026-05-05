class Solution:
    def isValid(self, s: str) -> bool:
        map1={'{':'}','(':')','[':']'}
        stack=[]
        if(len(s)<=1):
            return False

        for i in s:
            if i in map1:
                stack.append(i)
            else:
                
                if stack and map1[stack[-1]]==i:
                    stack.pop()
                else:
                    return False
        return not stack
        
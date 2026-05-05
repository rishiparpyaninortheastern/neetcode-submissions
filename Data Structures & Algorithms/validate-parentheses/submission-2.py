class Solution:
    def isValid(self, s: str) -> bool:
        maps={'[':']','{':'}','(':')'}

        stacks=[]
       
        for i in s:
            if i in maps.keys():
                stacks.append(i)
            else:
                if not stacks or maps[stacks.pop()] != i:
                    return False
        return not stacks
                 


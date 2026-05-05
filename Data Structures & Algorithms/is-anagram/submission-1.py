class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1=[0]*26
        arr2=[0]*26
        for i in s:
            c=ord(i)-ord('a')
            arr1[c]+=1
        for i in t:
            c=ord(i)-ord('a')
            arr2[c]+=1
        
        if arr1==arr2:
            return True
        else:
            return False


        
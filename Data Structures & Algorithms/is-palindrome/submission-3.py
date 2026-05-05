class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l,r=0,len(s)-1
        while l<r:
            while r > l and not self.isalpha(s[r]):
                r=r-1
            while l<r  and not self.isalpha(s[l]):
                l=l+1
            if s[l].lower()!=s[r].lower():
                return False
            l,r=l+1,r-1
        
        return True

            



    def isalpha(self,char):
        return (ord('a')<=ord(char)<=ord('z')
        or ord('A')<=ord(char)<=ord('Z')
        or ord('0')<=ord(char)<=ord('9'))
        
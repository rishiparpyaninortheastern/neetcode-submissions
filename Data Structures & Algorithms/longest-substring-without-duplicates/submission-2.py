class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       res=0
       
       for i in range(len(s)):
        resset=set()
        for j in range(i,len(s)):
            if s[j] in resset:
                break
            resset.add(s[j])
        res=max(res,len(resset))
       return res


        
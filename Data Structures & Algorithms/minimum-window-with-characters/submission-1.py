class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount={}
        for c in t:
            tcount[c]=tcount.get(c,0)+1
        have=0
        need=len(tcount)
        minlen=float('inf')
        scount={}
        l=0
        res=[-1,-1]
        for r in range(len(s)):
            if s[r] in tcount:
                scount[s[r]]=scount.get(s[r],0)+1
                if scount[s[r]]==tcount[s[r]]:
                    have+=1
        
            while have==need:
                if (r-l+1)<minlen:
                    minlen=r-l+1
                    res=[l,r]

                if s[l] in tcount:
                    if scount[s[l]]==tcount[s[l]]:
                        have-=1
                    
                    scount[s[l]]-=1
                l+=1
        l,r=res[0],res[1]
        return s[l:r+1] if minlen!=float('inf') else ''


        
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount={}

        for c in t:
            tcount[c]=tcount.get(c,0)+1
        scount={}
        l=0
        have=0
        reslen=float('inf')
        need=len(tcount)
        res=[-1,-1]

        for r in range(len(s)):

            if s[r] in tcount:
                scount[s[r]]=scount.get(s[r],0)+1
                if scount[s[r]]==tcount[s[r]]:
                    have+=1
            
            while have==need:
                if (r - l + 1) < reslen:   # fix
                    res = [l, r]
                    reslen = r - l + 1

                if s[l] in tcount:   # fix
                    if scount[s[l]] == tcount[s[l]]:
                        have -= 1
                    scount[s[l]] -= 1

                l+=1
        l, r = res
        return s[l:r+1] if reslen != float('inf') else ""

        
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        lmax,rmax=height[l],height[r]
        trap=0

        while l<r:
            if lmax<rmax:
                l+=1
                lmax=max(lmax,height[l])
                trap+=max(lmax-height[l],0)
            else:
                r-=1
                rmax=max(rmax,height[r])
                trap+=max(rmax-height[r],0)
        return trap

        
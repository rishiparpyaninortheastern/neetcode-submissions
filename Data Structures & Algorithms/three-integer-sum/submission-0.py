class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resf=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        res=[ nums[i],nums[j],nums[k]]
                        res=sorted(res)
                        if res not in resf:
                            resf.append(res)
        return resf


        
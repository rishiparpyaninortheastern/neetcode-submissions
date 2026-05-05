class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resf=[]
        for i in range(len(nums)):
            res=1
            for j in range(len(nums)):
                if i!=j:
                    res=res*nums[j]
            resf.append(res)
            print(res)
        return resf
        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x=len(set(nums))
        if x==len(nums):
            return False
        return True
         
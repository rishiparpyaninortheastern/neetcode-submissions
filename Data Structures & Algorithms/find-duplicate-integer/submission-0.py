class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map={}
        for i in nums:
            map[i]=map.get(i,0)+1

            if map[i]>1:
                return i
        
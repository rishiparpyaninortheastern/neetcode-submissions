class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map={}

        for i,v in enumerate(numbers):
            if target-v in map:
                return [map[target-v]+1,i+1]
            map[v]=i
        
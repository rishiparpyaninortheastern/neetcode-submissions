from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        # Traverse through the list once
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in index:
                # If the difference exists in the dictionary, return the pair of indices
                return [index[diff], i]
            # Store the index of the current number
            index[nums[i]] = i
        
        # If no solution exists, return an empty list (though the problem guarantees a solution)
        return []


        
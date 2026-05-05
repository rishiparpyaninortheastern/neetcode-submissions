import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right  # keep track of minimum valid speed

        while left <= right:
            mid = (left + right) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                result = mid  # mid is a valid speed, try slower
                right = mid - 1
            else:
                left = mid + 1

        return result

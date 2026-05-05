from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        arr = self.map[key]

        l, r = 0, len(arr) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2

            if arr[mid][1] <= timestamp:
                res = arr[mid][0]   # candidate
                l = mid + 1
            else:
                r = mid - 1

        return res
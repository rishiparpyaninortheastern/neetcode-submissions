class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for i in nums:
            if i not in map.keys():
                map[i]=1
            else:
                map[i]+=1
        sorted_map =sorted(map.items(), key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_map[i][0])  # Append the element (key) to the result
        
        return result


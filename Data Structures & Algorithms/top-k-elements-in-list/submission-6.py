class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map={}
        for i in nums:
            map[i]=map.get(i,0)+1
        print(map)
        map = sorted(map.items(), key=lambda x: (-x[1],x[0]))
        res=[]

        for i in range(k):
            res.append(map[i][0])

        print(map)
        return res
        
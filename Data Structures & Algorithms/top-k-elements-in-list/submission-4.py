class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for n in nums:
            if n not in map:
                map[n]=1
            else:
                map[n]+=1
        newmap=sorted(map.items(),key=lambda x: x[-1],reverse=True)
        print(newmap)
        res=[]
        for i in range (k):
            res.append(newmap[i][0])
        return res



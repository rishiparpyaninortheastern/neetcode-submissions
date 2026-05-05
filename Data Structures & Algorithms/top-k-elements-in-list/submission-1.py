class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for i in nums:
            if i not in map:
                map[i]=1
            else:
                map[i]+=1
    
        sorted_items =sorted(map.items(), key=lambda x: x[1], reverse=True)
        print(map)
        res=[]
        for i in range(k):
            res.append(sorted_items[i][0])
        return res

        
        
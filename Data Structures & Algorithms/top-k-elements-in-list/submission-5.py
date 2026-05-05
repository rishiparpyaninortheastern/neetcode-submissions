class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for i in nums:
            if i not in map:
                map[i]=1
            else:
                map[i]+=1
            
        nmap=sorted(map.items(), key= lambda x : -x[1])
        print(nmap)
        res=[]

        for i in range(k):
            res.append(nmap[i][0])
        return res



        
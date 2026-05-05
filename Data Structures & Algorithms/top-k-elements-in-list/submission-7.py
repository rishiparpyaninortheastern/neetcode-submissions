class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        print(count)
        maxheap=[(-freq,num)for num,freq in count.items()]
        heapq.heapify(maxheap)

        res=[]
        for i in range(k):
            c,n=heapq.heappop(maxheap)
            res.append(n)
        return res

        
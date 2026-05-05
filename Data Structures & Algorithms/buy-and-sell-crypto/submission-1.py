class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxn=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]<prices[j]:
                    maxn=max(maxn,prices[j]-prices[i])
        print(maxn)
        return maxn
        
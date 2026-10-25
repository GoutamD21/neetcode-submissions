class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # res = int
        # lo = 0 
        # hi = len(prices) - 1
        # profit = 0
        # while lo < hi:
        #     if prices[hi] - prices[lo] > 0 :
        #         profit = max(profit, prices[hi] - prices[lo])
        #         hi -= 1
        #     if prices[hi] - prices[lo] <= 0:
        #         lo += 1
        # return profit
        
        minprice = prices[0]
        maxprofit = 0

        for i, n in enumerate(prices):
            minprice = min(minprice, prices[i])
            maxprofit = max(maxprofit, prices[i] - minprice)

        return maxprofit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buyPrice: int = prices[0]
        profit: int = 0

        for currentPrice in prices:
            if currentPrice < buyPrice:
                buyPrice = currentPrice

            if (currentPrice - buyPrice) > profit:
                profit = currentPrice - buyPrice

        return profit
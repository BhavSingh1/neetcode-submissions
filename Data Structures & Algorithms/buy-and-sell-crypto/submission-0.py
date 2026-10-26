class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftCounter, rightCounter = 0, 1
        maxP = 0

        while rightCounter < len(prices):
            if prices[leftCounter] < prices[rightCounter]:
                profit = prices[rightCounter] - prices[leftCounter]
                maxP = max(maxP, profit)
            else:
                leftCounter = rightCounter
            rightCounter += 1
        return maxP

        
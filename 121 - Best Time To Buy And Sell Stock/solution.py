from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return self.twoPointer(prices)
        return self.onePass(prices)

    # Time O(n)
    # Space O(1)
    def twoPointer(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        l = 0
        r = 0
        while r < n:
            # Profit made, update tracker
            if prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
            # Loss made, shift left pointer over the subarray already processed
            else:
                l = r
            r += 1
        return profit

    # Time O(n)
    # Space O(1)
    def onePass(self, prices: List[int]) -> int:
        profit = 0
        lowestPx = prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - lowestPx)
            if prices[i] < lowestPx:
                lowestPx = prices[i]
        return profit
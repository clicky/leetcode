class Solution:

    # Must buy before sell
    # Either B/S or skip
    def maxProfit(self, prices: List[int]) -> int:
        # return self.recursion(prices, 0, True)
        dp = [[-1, -1] for i in range(len(prices))]
        return self.topDownMemo(prices, 0, dp, True)

    def recursion(self, prices: List[int], i: int, isBuy: bool) -> int:
        # Base case
        if i == len(prices):
            return 0
        profit = 0
        if isBuy:
            buy = self.recursion(prices, i + 1, False) - prices[i]
            skip = self.recursion(prices, i + 1, True)
            profit = max(buy, skip)
        else:
            sell = self.recursion(prices, i + 1, True) + prices[i]
            skip = self.recursion(prices, i + 1, False)
            profit = max(sell, skip)
        return profit

    def topDownMemo(self, prices: List[int], i: int, dp: [], isBuy: bool) -> int:
        # Base case
        if i == len(prices):
            return 0
        # Memoisation
        idx = 1 if isBuy else 0
        if dp[i][idx] != -1:
            return dp[i][idx]
        # Branch
        profit = 0
        if isBuy:
            # Buy
            buy = self.topDownMemo(prices, i + 1, dp, False) - prices[i]
            # Skip
            skip = self.topDownMemo(prices, i + 1, dp, True)
            profit = max(buy, skip)
        else:
            # Sell
            sell = self.topDownMemo(prices, i + 1, dp, True) + prices[i]
            # Skip
            skip = self.topDownMemo(prices, i + 1, dp, False)
            profit = max(sell, skip)
        dp[i][idx] = profit
        return profit
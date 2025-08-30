from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        # return self.recursion(prices, 0, True)
        # dp = [[-1,-1] for i in range(len(prices))]
        # return self.topDown(prices, 0, dp, True)
        # return self.bottomUp(prices)
        return self.greedy(prices)

    # Must either buy or sell, but cant sell before buying. So keep track of side for current iteration
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

    def topDown(self, prices: List[int], i: int, dp: [], isBuy: bool) -> int:
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

    # Bottom up refers to building a 2D matrix and working from the bottom up to (0,0)
    # If the recursive/top down approach looks forward then bottom up will have a loop going backwards
    # The coordinates of the final call always match the first call into the recursive/top down solution
    def bottomUp(self, prices: List[int]) -> int:
        # We need an extra row as we are looking forward. Row at idx 0 is computed from idx 1 etc so we need n+1
        n = len(prices)
        dp = [[0, 0] for i in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(2):
                profit = 0
                # Buy
                if j == 0:
                    buy = dp[i + 1][1] - prices[i]
                    skip = dp[i + 1][0]
                    profit = max(buy, skip)
                else:
                    sell = dp[i + 1][0] + prices[i]
                    skip = dp[i + 1][1]
                    profit = max(sell, skip)
                dp[i][j] = profit

        return dp[0][0]

    def greedy(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
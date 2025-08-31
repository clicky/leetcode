from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # res = self.recursive(coins, amount)
        # dp = [-1 for i in range(amount+1)]
        # res = self.memoTopDown(coins, amount, dp)
        res = self.tabBottomUp(coins, amount)
        return res if res <= amount else -1

    def recursive(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return amount + 1
        count = amount + 1
        for i in range(len(coins)):
            residual = amount - coins[i]
            curr = self.recursive(coins, residual)
            if curr != residual + 1:
                count = min(count, curr + 1)
        return count

    def memoTopDown(self, coins: List[int], amount: int, dp: []) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return amount + 1
        if dp[amount] != -1:
            return dp[amount]
        count = amount + 1
        for i in range(len(coins)):
            residual = amount - coins[i]
            curr = self.memoTopDown(coins, residual, dp)
            if curr != residual + 1:
                count = min(count, curr + 1)
        dp[amount] = count
        return count

    def tabBottomUp(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for i in range(amount + 1)]
        dp[0] = 0
        for i in range(1, len(dp)):
            for j in range(len(coins)):
                if i - coins[j] >= 0 and dp[i - coins[j]] != amount + 1:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        return dp[amount]

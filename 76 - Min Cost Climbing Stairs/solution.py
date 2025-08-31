from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # return min(self.recursive(cost, 0), self.recursive(cost, 1))
        # dp = [-1 for i in range(len(cost))]
        # return min(self.memoTopDown(cost, 0, dp), self.memoTopDown(cost, 1, dp))
        # return self.tabBottomUp(cost)
        return self.optimised(cost)

    def recursive(self, cost: List[int], i: int) -> int:
        if i >= len(cost):
            return 0
        one = self.recursive(cost, i + 1) + cost[i]
        two = self.recursive(cost, i + 2) + cost[i]
        return min(one, two)

    def memoTopDown(self, cost: List[int], i: int, dp: []) -> int:
        if i >= len(cost):
            return 0
        if dp[i] != -1:
            return dp[i]
        one = self.memoTopDown(cost, i + 1, dp) + cost[i]
        two = self.memoTopDown(cost, i + 2, dp) + cost[i]
        dp[i] = min(one, two)
        return dp[i]

    def tabBottomUp(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0 for i in range(n)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[n - 1], dp[n - 2])

    def optimised(self, cost: List[int]) -> int:
        n = len(cost)
        prev1 = cost[1]
        prev2 = cost[0]
        for i in range(2, n):
            curr = min(prev1, prev2) + cost[i]
            prev2 = prev1
            prev1 = curr
        return min(prev1, prev2)

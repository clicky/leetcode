from typing import List

class Solution:

    def jump(self, nums: List[int]) -> int:
        # return self.recursive(nums, 0)
        # dp = [-1] * len(nums)
        # return self.memoBottomUp(nums, 0, dp)
        return self.greedy(nums)

    def recursive(self, nums: List[int], i: int) -> int:
        if i >= len(nums) - 1:
            return 0
        min_count = len(nums)
        for j in range(nums[i], 0, -1):
            curr = self.recursive(nums, i + j)
            min_count = min(min_count, curr + 1)
        return min_count

    def memoBottomUp(self, nums: List[int], i: int, dp: []) -> int:
        if i >= len(nums) - 1:
            return 0
        if dp[i] != -1:
            return dp[i]
        min_count = len(nums)
        for j in range(nums[i], 0, -1):
            curr = self.memoBottomUp(nums, i + j, dp)
            min_count = min(min_count, curr + 1)
        dp[i] = min_count
        return min_count

    # Perform a BFS using two pointers.
    # Each level of the BFS is width of reachable indexes from the previous level. First level is just index 0.
    def greedy(self, nums: List[int]) -> int:
        levels = 0
        l = 0
        r = 0
        # Number of levels is greater than number of jumps required so only go up to n-2
        while r < len(nums) - 1:
            furthest = r + 1
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            l = r + 1
            r = furthest
            levels += 1
        return levels
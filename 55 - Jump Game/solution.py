from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # return self.greedyBottomUp(nums)
        # return self.greedyTopDown(nums)
        # return self.recursive(nums, len(nums)-1)
        dp = [-1 for i in range(len(nums))]
        # return self.memoTopDown(nums, len(nums)-1, dp)
        return self.memoBottomUp(nums, 0, dp)

    def greedyBottomUp(self, nums: List[int]) -> bool:
        curr = 0
        for i in range(len(nums)):
            # Previous value was 0 / we have come too far (hit unreachable element)
            if i > curr:
                return False
            # Update max reach based on current and max jump from i
            curr = max(curr, i + nums[i])
        # Return True to avoid complex checks around edge cases
        # Handle the False case inside of the loop
        return True

    def greedyTopDown(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1
        # Starting goal is the last element.
        # Work backwards by iterating over the remaining elements to see if you can hit the goal.
        # Once you hit the goal, reset to the goal to the current element and repeat.
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= goal:
                # We know from pos i the goal can be hit
                # Sub problem is can you get to i from '<i'
                goal = i
        return goal == 0

    def recursiveTopDown(self, nums: List[int], goal: int) -> bool:
        if goal == 0:
            return True
        for i in range(goal - 1, -1, -1):
            if i + nums[i] >= goal:
                res = self.recursive(nums, i)
                if res:
                    return True
        return False

    def memoTopDown(self, nums: List[int], goal: int, dp: []) -> bool:
        if goal == 0:
            return True
        if dp[goal] != -1:
            return dp[goal] == 1
        res = False
        for i in range(goal - 1, -1, -1):
            if i + nums[i] >= goal:
                res |= self.memoTopDown(nums, i, dp)
                if res:
                    break
        dp[goal] = 1 if res else 0
        return res

    def memoBottomUp(self, nums: List[int], i: int, dp: []) -> bool:
        if i >= len(nums) - 1:
            return True
        if dp[i] != -1:
            return dp[i] == 1
        # Greedily checking recursively from a further ahead starting point
        res = False
        # Already define dp[0] so loop j from nums[i] till >0
        for j in range(nums[i], 0, -1):
            res |= self.memoBottomUp(nums, i + j, dp)
            if res:
                break
        dp[i] = 1 if res else 0
        return res
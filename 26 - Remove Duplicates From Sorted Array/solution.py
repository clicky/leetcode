from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        t = 1
        for r in range(1, n):
            # Find where value changes and update the tail element
            if nums[r] != nums[r-1]:
                nums[t] = nums[r]
                t += 1
        return t
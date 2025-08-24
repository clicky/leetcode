from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        t = 0
        r = 0
        while r < n:
            # Count number of duplicates
            count = 1
            while (r+1) < n and nums[r] == nums[r+1]:
                r += 1
                count += 1
            # Populate the duplicates
            for i in range(min(2, count)):
                nums[t] = nums[r]
                t += 1
            # Shift pointer for next number
            r += 1
        return t
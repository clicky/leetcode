from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # return self.mapImpl(nums)
        return self.boyerMooreVotingImpl(nums)

    # Time O(n)
    # Space O(n)
    def mapImpl(self, nums: List[int]) -> int:
        majorityElement = nums[0]
        majorityCount = 1
        m = dict()
        for n in nums:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1
            if m[n] > majorityCount:
                majorityCount = m[n]
                majorityElement = n
        return majorityElement

    # Time O(n)
    # Space O(1)
    # Iterate over array and increase counter when you see a repeat digit and decrement for each different digit.
    # Reset the digit being compared when the count is decremented to zero.
    # Intuition is that all non-majority elements will have their count reset to 0 and the remaining will be left
    # as it has a count of floor(n/2).
    def boyerMooreVotingImpl(self, nums: List[int]) -> int:
        majorityCount = 0
        majorityElement = 0
        for n in nums:
            if majorityCount == 0:
                majorityElement = n
            if majorityElement == n:
                majorityCount += 1
            else:
                majorityCount -= 1
        return majorityElement
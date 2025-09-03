from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1] * n

        # Prefix check
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                # You cant just do res += 1
                # Because res[i-1] has previously been potentially incremented
                res[i] = res[i - 1] + 1

        # Suffix check
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # Because this is the second pass, use max check
                res[i] = max(res[i], res[i + 1] + 1)

        return sum(res)

from typing import List

class Solution:

    def hIndex(self, citations: List[int]) -> int:
        return self.countSearch(citations)

    def countSearch(self, citations: List[int]) -> int:
        n = len(citations)
        # At most h index can be n if each paper has at least n citations
        # Create a freq array for n+1 because we need to account for papers with 0 citations
        freq = [0] * (n + 1)
        for i in range(n):
            idx = min(n, citations[i])
            freq[idx] += 1
        # We want the highest h so work backwards starting with h=n
        # If cumulative freq < h then decrement h, update freq and keep going
        h = n
        papers = freq[n]
        while papers < h:
            h -= 1
            papers += freq[h]
        return h

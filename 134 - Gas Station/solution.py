from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # return self.bruteForce(gas, cost)
        return self.greedy(gas, cost)

    def bruteForce(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        def run(start: int) -> bool:
            tank = 0
            for i in range(n):
                idx = (start + i) % n
                tank += gas[idx]
                if tank < cost[idx]:
                    return False
                tank -= cost[idx]
            return True

        for i in range(n):
            if run(i):
                return i
        return -1

    # In one pass iterate over the arrays to get total gas - total cost.
    # If the total cost is greater than total gas then there is no solution.
    # Also seperately track the current gas tank capacity. When this becomes negative
    # use Kadane's to reset and shift the starting position.
    def greedy(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        start = 0
        tank = 0
        totalGas = 0

        for i in range(n):
            remaining = gas[i] - cost[i]
            tank += remaining
            totalGas += remaining
            # Kadane's algorithm
            if tank < 0:
                tank = 0
                start = (i + 1) % n

        return start if totalGas >= 0 else -1

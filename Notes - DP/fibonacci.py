# Time O(2^n)
# Space O(n)
def recursive(n: int) -> int:
    if n <= 1:
        return n
    return recursive(n-1) + recursive(n-2)

# Time O(n)
# Space O(n)
def topDownMemoization(n: int, dp: []) -> int:
    if n <= 1:
        return n
    if dp[n] > -1:
        return dp[n]
    dp[n] = topDownMemoization(n-1, dp) + topDownMemoization(n, dp)
    return dp[n]

# Time O(n)
# Space O(n)
def bottomUpTabulation(n: int) -> int:
    if n <= 1:
        return n
    dp = [0,1]
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Time O(n)
# Space O(1)
def bottomUpSpaceOptimised(n: int) -> int:
    if n <= 1:
        return n
    prev1 = 1
    prev2 = 0
    for i in range(2, n+1):
        curr = prev1 + prev2
        prev1 = curr
        prev2 = prev1
    return prev1

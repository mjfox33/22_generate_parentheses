class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        dp = [[] for _ in range(n+1)]
        dp[0] = ['']
        for i in range(1,n+1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i-j-1]]
        return dp[-1]
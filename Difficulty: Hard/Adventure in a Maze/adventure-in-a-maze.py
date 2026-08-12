class Solution:
    def findWays(self, grid):
        n = len(grid)
        MOD = 10**9 + 7

        dp = [[(0, 0) for _ in range(n)] for _ in range(n)]
        dp[0][0] = (1, grid[0][0])

        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                paths = 0
                max_adventure = -1

                # Move Down from top cell
                if i > 0 and grid[i - 1][j] in (2, 3):
                    p, a = dp[i - 1][j]
                    if p > 0:
                        paths = (paths + p) % MOD
                        max_adventure = max(max_adventure, a)

                # Move Right from left cell
                if j > 0 and grid[i][j - 1] in (1, 3):
                    p, a = dp[i][j - 1]
                    if p > 0:
                        paths = (paths + p) % MOD
                        max_adventure = max(max_adventure, a)

                if paths > 0:
                    dp[i][j] = (
                        paths,
                        max_adventure + grid[i][j]
                    )

        paths, adventure = dp[n - 1][n - 1]

        if paths == 0:
            return [0, 0]

        return [paths, adventure]
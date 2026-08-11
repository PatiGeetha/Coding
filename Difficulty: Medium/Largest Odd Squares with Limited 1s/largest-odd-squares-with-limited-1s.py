class Solution:
    def largestSquare(self, mat: list[list[int]], queries: list[list[int]], k: int) -> list[int]:
        n = len(mat)
        m = len(mat[0])

        # Prefix sum
        prefix = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        def square_sum(r, c, size):
            half = size // 2

            r1 = r - half
            c1 = c - half
            r2 = r + half
            c2 = c + half

            return (
                prefix[r2 + 1][c2 + 1]
                - prefix[r1][c2 + 1]
                - prefix[r2 + 1][c1]
                + prefix[r1][c1]
            )

        ans = []

        for r, c in queries:
            # Maximum possible radius
            max_radius = min(r, c, n - 1 - r, m - 1 - c)

            # If even 1x1 square is not valid
            if mat[r][c] > k:
                ans.append(-1)
                continue

            low = 0
            high = max_radius
            best = 0

            # Binary search radius
            while low <= high:
                mid = (low + high) // 2
                size = 2 * mid + 1

                if square_sum(r, c, size) <= k:
                    best = size
                    low = mid + 1
                else:
                    high = mid - 1

            ans.append(best)

        return ans
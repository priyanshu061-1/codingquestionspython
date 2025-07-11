def f(i, j, dp):
    if i < 0 or j < 0:
        return 0
    if i == 0 and j == 0:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]

    up = f(i - 1, j, dp)
    left = f(i, j - 1, dp)
    dp[i][j] = up + left
    return dp[i][j]

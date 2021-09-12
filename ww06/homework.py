"""
    dynamic programming
"""


# minimum path sum
def min_path_sum(grid):
    # divide/ subproblem
    # define status array  grid[i][j]:min-path-sum starting from row-i, col-j
    # inference formula   grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

    row = len(grid)
    col = len(grid[0])
    if row == 0: return 0
    if col == 0: return sum(grid)
    for i in range(row):
        for j in range(col):
            if i == j == 0:
                continue
            elif j == 0:
                grid[i][j] += grid[i - 1][j]
            elif i == 0:
                grid[i][j] += grid[i][j - 1]
            else:
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

    return grid[row - 1][col - 1]


# decoder method
def num_decodings(s):
    n = len(s)
    s = ' ' + s
    f = [0] * (n + 1)
    f[0] = 1
    for i in range(1, n + 1):
        a = ord(s[i]) - ord('0')
        b = (ord(s[i - 1]) - ord('0')) * 10 + ord(s[i]) - ord('0')
        if 1 <= a <= 9:
            f[i] = f[i - 1]
        if 10 <= b <= 26:
            f[i] += f[i - 2]
    return f[n]
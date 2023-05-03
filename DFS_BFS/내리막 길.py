# BOJ 1520 골드3
# DFS + DP
import sys


def dfs(x, y):
    global answer
    if (x, y) == (n - 1, m - 1):
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    count = 0
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] < graph[x][y]:
            count += dfs(nx, ny)

    dp[x][y] = count
    return dp[x][y]

if __name__ == "__main__":
    sys.setrecursionlimit(10**4)
    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    dp = [[-1] * m for _ in range(n)]
    
    print(dfs(0, 0))
    
    # for i in range(n):
    #     print(dp[i])
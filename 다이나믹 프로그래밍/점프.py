N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for x in range(N):
    for y in range(N):
        if graph[x][y] == 0:
            continue
        if (dx := x + graph[x][y]) < N:
            dp[dx][y] += dp[x][y]
        if (dy := y + graph[x][y]) < N:
            dp[x][dy] += dp[x][y]

print(dp[N-1][N-1])

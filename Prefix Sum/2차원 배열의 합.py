n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


p_sum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        p_sum[i + 1][j + 1] = p_sum[i][j + 1] + p_sum[i + 1][j] + arr[i][j] - p_sum[i][j]

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    print(p_sum[x2][y2] - p_sum[x1 - 1][y2] - p_sum[x2][y1 - 1] + p_sum[x1 - 1][y1 - 1])

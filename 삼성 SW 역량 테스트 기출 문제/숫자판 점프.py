# BOJ 2210
# 백트래킹
arr = [(list(map(int, input().split()))) for _ in range(5)]
ans = set()
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(x, y, s):
    s += str(arr[x][y])
    if len(s) == 6:
        ans.add(s)
        return
    for dx, dy in d:
        nx = dx + x
        ny = dy + y
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, s)


for i in range(5):
    for j in range(5):
        dfs(i, j, "")

print(len(ans))

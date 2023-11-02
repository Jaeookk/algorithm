# dfs, bfs 다 가능. 단, bfs시 queue가 아니라 set을 이용

import sys

input = sys.stdin.readline

r, c = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(r)]
ans = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

in_range = lambda x, y: 0 <= x < r and 0 <= y < c


def bfs():
    global ans
    q = set([(0, 0, maps[0][0])])
    while q:
        x, y, alpha = q.pop()
        ans = max(ans, len(alpha))

        if ans == 26:
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny) and maps[nx][ny] not in alpha:
                q.add((nx, ny, alpha + maps[nx][ny]))


bfs()
print(ans)

# def dfs(x, y, count):
#     global ans
#     ans = max(ans, count)
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < r and 0 <= ny < c and not maps[nx][ny] in alphas:
#             alphas.add(maps[nx][ny])
#             dfs(nx, ny, count + 1)
#             alphas.remove(maps[nx][ny])


# alphas.add(maps[0][0])
# dfs(0, 0, 1)
# print(ans)

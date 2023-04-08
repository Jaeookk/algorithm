import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(r)]


def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    visited = [[False for _ in range(c)] for _ in range(r)]
    visited[x][y] = True
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while q:
        x, y, count = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == "L" and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, count + 1))
    return count


answer = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == "L":  # 육지일때
            # 해당 좌표가 육지의 끝단이 아니라면 어차피 보물이 묻힐 조건이 성립되지 않기 때문에 미리 거르기
            # 이 최적화 작업을 안 할시 python3에서 시간초과.
            if 0 <= i - 1 < r and 0 <= i + 1 < r and graph[i - 1][j] == "L" and graph[i + 1][j] == "L":
                continue
            if 0 <= j - 1 < c and 0 <= j + 1 < c and graph[i][j - 1] == "L" and graph[i][j + 1] == "L":
                continue
            answer = max(bfs(i, j), answer)

print(answer)

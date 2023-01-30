from collections import deque


def bfs(graph, x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        zero_cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] != 0:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                if graph[nx][ny] == 0:
                    zero_cnt += 1
        if zero_cnt > 0:
            graph[x][y] -= zero_cnt
            if graph[x][y] < 0:
                graph[x][y] = 0
    return 1


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    year = 0

    while True:
        visited = [[False] * m for _ in range(n)]
        num_bfs = 0
        flag = False
        for i in range(n):
            for j in range(m):
                if graph[i][j] != 0:
                    flag = True
                    if not visited[i][j]:
                        num_bfs += bfs(graph, i, j, visited)
        if num_bfs >= 2:  # 빙산의 개수가 2개 이상이라면 중지
            break
        if not flag:  # 빙산이 모두 녹았다면
            year = 0
            break
        year += 1

    print(year)

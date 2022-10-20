from collections import deque


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1


def bfs(x, y, flag):
    q = deque()
    q.append((x, y, flag))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y, flag = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][flag]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and flag == 0:
                    # 다음 이동할 곳이 벽이고, 벽을 아직 부시지 않은 경우
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx, ny, 1))
                elif graph[nx][ny] == 0 and visited[nx][ny][flag] == 0:
                    # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
                    visited[nx][ny][flag] = visited[x][y][flag] + 1
                    q.append((nx, ny, flag))
    return -1


print(bfs(0, 0, 0))

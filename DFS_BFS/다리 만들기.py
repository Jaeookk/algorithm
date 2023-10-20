from collections import deque


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


# 나라 구분을 하고

# 각 나라마다의 최단 거리를 구한다.


in_range = lambda x, y: 0 <= x < N and 0 <= y < N


def distinguish_nation(r, c, num):
    global visited

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    q = deque([(r, c)])
    visited[r][c] = True
    graph[r][c] = num

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny) and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
                graph[nx][ny] = num


def get_shortest_dist(num):
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    q = deque()
    dist = [[-1] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if graph[r][c] == num:  # r,c가 num나라이면 거리는 0으로 초기화 시키고 큐에 담기
                dist[r][c] = 0
                q.append((r, c))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny):
                if graph[nx][ny] and graph[nx][ny] != num:  # 다른나라와 연결
                    return dist[x][y]

                elif not graph[nx][ny] and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))


visited = [[False] * N for _ in range(N)]
nation = 1
answer = 1e10

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            distinguish_nation(i, j, nation)
            nation += 1

for k in range(1, nation):
    answer = min(answer, get_shortest_dist(k))
print(answer)

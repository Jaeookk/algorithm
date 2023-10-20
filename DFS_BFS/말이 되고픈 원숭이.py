from collections import deque


K = int(input())
W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]  # 0:평지 , 1:장애물
in_range = lambda x, y: 0 <= x < H and 0 <= y < W


def bfs():
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    dhx, dhy = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, 2, 1, -1, -2]
    q = deque([(0, 0, 0)])

    # 기존의 2차원 visited 배열에 1개 차원을 더 추가하여 말의 이동수단을 z번 썻을때의 거리를 구하자.
    visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
    visited[0][0][0] = 1

    while q:
        x, y, z = q.popleft()

        if x == H - 1 and y == W - 1:
            return visited[x][y][z] - 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if in_range(nx, ny) and not visited[nx][ny][z] and not graph[nx][ny]:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx, ny, z))

        if z < K:  # 아직 말의 움직임을 다 사용하지 않았다면
            for j in range(8):
                hx, hy = x + dhx[j], y + dhy[j]
                if in_range(hx, hy) and not visited[hx][hy][z + 1] and not graph[hx][hy]:
                    # 범위에 있고, 도착지점이 장애물이 아니고, z+1번 말의 움직임을 사용하여 도착한 곳이 아니라면
                    visited[hx][hy][z + 1] = visited[x][y][z] + 1
                    q.append((hx, hy, z + 1))

    return -1


print(bfs())

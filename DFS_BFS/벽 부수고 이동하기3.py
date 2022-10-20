from collections import deque
import sys

input = sys.stdin.readline


n, m, k = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
visited[0][0] = [1 for _ in range(k + 1)]


def bfs(x, y, flag, dist):
    """
    x : 행
    y : 형
    flag : 벽을 부순 횟수
    dist : 거리
    """
    q = deque()
    q.append((x, y, flag, dist))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    day = 1  # 1은 낮, -1은 밤

    while q:
        
        # 하루에 발생할 수 있는 모든 경우의 수를 처리하여야 하므로 같은 시점(같은 시간)이면 같이 처리를 해줘야한다.
        for _ in range(len(q)):
            x, y, flag, dist = q.popleft()
            if x == n - 1 and y == m - 1:
                return dist

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][flag]:
                    if graph[nx][ny] == 1:
                        # 다음 이동할 곳이 벽이고
                        if flag + 1 <= k and not visited[nx][ny][flag + 1]:
                            if day == 1:
                                visited[nx][ny][flag + 1] = dist + 1
                                q.append((nx, ny, flag + 1, dist + 1))
                            else:
                                q.append((x, y, flag, dist + 1))

                    elif graph[nx][ny] == 0:
                        # 다음 이동할 곳이 벽이 아니고
                        visited[nx][ny][flag] = dist + 1
                        q.append((nx, ny, flag, dist + 1))
        day *= -1
    return -1


print(bfs(0, 0, 0, 1))

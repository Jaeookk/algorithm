import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while f_queue:  # fire BFS
        x, y = f_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if f_visited[nx][ny] == -1 and graph[nx][ny] != "#":
                    f_visited[nx][ny] = f_visited[x][y] + 1
                    f_queue.append((nx, ny))

    while j_queue:  # jihoon BFS
        x, y = j_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if j_visited[nx][ny] == -1 and graph[nx][ny] != "#":
                    if f_visited[nx][ny] == -1 or f_visited[nx][ny] > j_visited[x][y] + 1:
                        # 불이 있지 않거나, 아직 불이 도달하기 전이라면
                        j_visited[nx][ny] = j_visited[x][y] + 1
                        j_queue.append((nx, ny))
            else:
                return j_visited[x][y] + 1  # escape map

    return "IMPOSSIBLE"  # not escape map


r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
f_queue, j_queue = deque(), deque()  # declare fire, jihoon queue
f_visited, j_visited = [[-1] * c for _ in range(r)], [[-1] * c for _ in range(r)]  # declare fire, jihoon visited

for i in range(r):
    for j in range(c):
        if graph[i][j] == "F":
            f_queue.append((i, j))
            f_visited[i][j] = 0
        elif graph[i][j] == "J":
            j_queue.append((i, j))
            j_visited[i][j] = 0
print(bfs())

# # 시간초과 풀이
# from collections import deque
# import sys
# import copy

# input = sys.stdin.readline

# r, c = map(int, input().split())
# graph = [list(input().rstrip()) for _ in range(r)]
# visited = [[False] * c for _ in range(r)]


# def bfs():
#     flag = False
#     q = deque()
#     F = deque()
#     for i in range(r):
#         for j in range(c):
#             if graph[i][j] == "J":
#                 q.append((i, j, 0))
#                 visited[i][j] = True
#             elif graph[i][j] == "F":
#                 F.append((i, j, 0))
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     while q:
#         x, y, time = q.popleft()
#         for i in copy.deepcopy(F):
#             if i[2] == time:
#                 fx, fy, ftime = F.popleft()
#                 for i in range(4):
#                     nfx = fx + dx[i]
#                     nfy = fy + dy[i]
#                     if 0 <= nfx < r and 0 <= nfy < c and graph[nfx][nfy] != "#":
#                         if graph[nfx][nfy] != "F":
#                             graph[nfx][nfy] = "F"
#                             F.append((nfx, nfy, ftime + 1))
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != "#":
#                 if graph[nx][ny] != "F" and visited[nx][ny] != True:
#                     q.append((nx, ny, time + 1))
#                     visited[nx][ny] = True
#                     print(nx, ny, time + 1)
#                     if nx == 0 or nx == r - 1 or ny == 0 or ny == c - 1:
#                         return time + 1
#     return -1

# result = bfs()
# if result == -1:
#     print("IMPOSSIBLE")
# else:
#     print(result + 1)

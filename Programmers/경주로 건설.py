# 2020 카카오 인턴십
# 프로그래머스 LV.3

from collections import deque


def solution(board):
    answer = int(1e9)
    n = len(board)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    # x,y,direction,cost
    q.append((0, 0, -1, 0))
    visited = {(0, 0, 0): 0, (0, 0, 1): 0, (0, 0, 2): 0, (0, 0, 3): 0}
    while q:
        x, y, direction, cost = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx and nx < n and 0 <= ny and ny < n and not board[nx][ny]:
                if (direction - d) % 2 == 0 or direction == -1:
                    new_cost = cost + 100
                else:
                    new_cost = cost + 600

                if nx == n - 1 and ny == n - 1:
                    answer = min(answer, new_cost)
                elif visited.get((nx, ny, d)) is None or visited.get((nx, ny, d)) > new_cost:
                    visited[(nx, ny, d)] = new_cost
                    q.append((nx, ny, d, new_cost))

    return answer


# import sys

# def dfs(x, y, ex, ey, cost, result, board, n, visited):
#     if x == n-1 and y == n-1:
#         if cost < result:
#             result = cost
#         return result

#     dir = [[1,0],[-1,0],[0,-1],[0,1]] # 상,하,좌,우

#     for i in range(4):
#         dx, dy = dir[i][0], dir[i][1]
#         nx, ny = x + dx, y + dy
#         if 0<= nx < n and 0<= ny < n and board[nx][ny] == 0:
#             if not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 if ex*dx == 0 and ey*dy == 0:   # corner
#                     result = dfs(nx, ny, dx, dy, cost + 600, result,board, n, visited)
#                 else:
#                     result = dfs(nx, ny, dx, dy, cost + 100, result,board, n, visited)
#                 visited[nx][ny] = False

#     return result
# def solution(board):
#     answer = 0
#     n = len(board)
#     visited = [[False for _ in range(n)] for _ in range(n)]


#     answer = dfs(0,0,0,0,-500, 1e9, board, n, visited)


#     return answer

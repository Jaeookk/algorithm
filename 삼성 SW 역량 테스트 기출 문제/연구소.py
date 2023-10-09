import sys
from collections import deque

f = sys.stdin.readline
n, m = map(int, f().split())

graph = []
for _ in range(n):
    a = list(map(int, f().split()))
    graph.append(a)

wall_possible = []
virus = []


def get_combinations(arr, n):
    result = []

    if n == 0:
        return [[]]  # []를 해버리면 C가 있는 for문에서 바로 종료됨. [[]]를 해야 for C in [[]]: 가 되어 C=[]가 된다.

    for i in range(0, len(arr)):
        elem = arr[i]
        rest_arr = arr[i + 1:]
        for C in get_combinations(rest_arr, n - 1):
            result.append([elem] + C)
            # print(f"n = {n}, elem = {elem}, rest_arr = {rest_arr}, result = {result}, C = {C}")

    return result


for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i, j))
        elif graph[i][j] == 0:
            wall_possible.append((i, j))

wall_combi = get_combinations(wall_possible, 3)
# print(wall_combi[0])


def bfs(safe_count):  # 바이러스 퍼트리기
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 4가지 방향에 대하여
    q = deque(virus)
    visited = [[False for _ in range(m)] for _ in range(n)]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    safe_count -= 1
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return safe_count


def solution():
    result = 0

    for datas in wall_combi:
        for i, j in datas:
            graph[i][j] = 1

        result = max(result, bfs(len(wall_possible) - 3))

        for i, j in datas:
            graph[i][j] = 0

    return result


print(solution())

# L(1 ≤ L ≤ 30)은 상범 빌딩의 층 수이다.
# R(1 ≤ R ≤ 30)과 C(1 ≤ C ≤ 30)는 상범 빌딩의 한 층의 행과 열의 개수를 나타낸다.
# 금으로 막혀있어 지나갈 수 없는 칸은 '#'으로 표현되고, 비어있는 칸은 '.'으로 표현
# 당신의 시작 지점은 'S'로 표현되고, 탈출할 수 있는 출구는 'E'로 표현된다

from collections import deque


def bfs(z, x, y):
    q = deque()
    q.append((x, y, z))
    visited[z][x][y] = 0
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < r and 0 <= ny < c and 0 <= nz < l:
                if visited[nz][nx][ny] == -1 and graph[nz][nx][ny] != "#":
                    q.append((nx, ny, nz))
                    visited[nz][nx][ny] = visited[z][x][y] + 1


if __name__ == "__main__":
    while True:
        l, r, c = map(int, input().split())
        if l == 0 and r == 0 and c == 0:
            break
        graph = []
        for _ in range(l):
            temp = []
            for _ in range(r + 1):
                temp2 = list(input())
                if temp2:
                    temp.append(temp2)
            graph.append(temp)

        visited = [[[-1 for _ in range(c)] for _ in range(r)] for _ in range(l)]

        for i in range(l):  # z
            for j in range(r):  # x
                for k in range(c):  # y
                    if graph[i][j][k] == "S":
                        bfs(i, j, k)
                    if graph[i][j][k] == "E":
                        escape = (i, j, k)

        i, j, k = escape
        if visited[i][j][k] == -1:
            print("Trapped!")
        else:
            print(f"Escaped in {visited[i][j][k]} minute(s).")

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

directions = list(map(int, input().split()))  # 1:동 2:서 3:북 4:남

cube = [[0 for _ in range(3)] for _ in range(4)]


def move(direction):
    if direction == 3:
        cube[0][1], cube[1][1], cube[2][1], cube[3][1] = (
            cube[1][1],
            cube[2][1],
            cube[3][1],
            cube[0][1],
        )
    elif direction == 1:
        cube[1][0], cube[1][1], cube[1][2], cube[3][1] = (
            cube[3][1],
            cube[1][0],
            cube[1][1],
            cube[1][2],
        )
    elif direction == 2:
        cube[3][1], cube[1][0], cube[1][1], cube[1][2] = (
            cube[1][0],
            cube[1][1],
            cube[1][2],
            cube[3][1],
        )
    else:
        cube[1][1], cube[2][1], cube[3][1], cube[0][1] = (
            cube[0][1],
            cube[1][1],
            cube[2][1],
            cube[3][1],
        )
    return cube


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cube[3][1] = graph[x][y]

for direction in directions:
    nx = x + dx[direction - 1]
    ny = y + dy[direction - 1]
    if 0 <= nx < n and 0 <= ny < m:
        cube = move(direction)
        if graph[nx][ny] == 0:
            graph[nx][ny] = cube[3][1]
        else:
            cube[3][1] = graph[nx][ny]
            graph[nx][ny] = 0
        x, y = nx, ny
        print(cube[1][1])

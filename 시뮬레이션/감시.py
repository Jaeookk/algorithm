import copy

n, m = map(int, input().split())
cctv = []
graph = []
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 3], [3, 1], [1, 2], [2, 0]],
    [[0, 2, 3], [0, 3, 1], [3, 1, 2], [1, 2, 0]],
    [[0, 1, 2, 3]],
]

# 북 - 남 - 서 - 동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])  # (cctv 번호, x좌표, y좌표)


def fill(board, mm, x, y):
    """
    board : 사무실
    mm : cctv의 감시 방향 0:북 1:남 2:서 3:동
    x : 해당 cctv 행 위치
    y : 해당 cctv 열 위치
    """
    for i in mm:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = "#"


def dfs(depth, arr):
    global min_value

    if depth == len(cctv):
        count = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    count += 1
            # count += arr[i].count(0)
        min_value = min(min_value, count)
        return

    temp = copy.deepcopy(arr)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        fill(temp, i, x, y)  # cctv로 graph 채우기
        dfs(depth + 1, temp)  # 백 트래킹
        temp = copy.deepcopy(arr)  # fill 함수로 채우기 전의 graph로 바꾸기


min_value = int(1e9)
dfs(0, graph)
print(min_value)

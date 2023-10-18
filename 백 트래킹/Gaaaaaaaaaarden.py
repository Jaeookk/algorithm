from collections import deque
import copy


N, M, G, R = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
board = [["O"] * M for _ in range(N)]
can_bayang = []
visited = [[False] * M for _ in range(N)]
answer = 0


for r in range(N):
    for c in range(M):
        if graph[r][c] == 2:  # 0:호수, 1:배양액X, 2:배양액O
            can_bayang.append((r, c))
        if graph[r][c] == 0:
            board[r][c] = "L"


in_range = lambda x, y: 0 <= x < N and 0 <= y < M


# 1. 황토색 칸에 배양액을 뿌려야 하는 모든 조합 찾기
def backtracking(start, r, g, result):
    global answer

    if r + g == R + G:
        # BFS 실시하여 꽃 개수 세기
        answer = max(answer, bfs(result))
        return

    for i in range(start, len(can_bayang)):
        row, col = can_bayang[i]
        if not visited[row][col]:
            if g < G:
                visited[row][col] = True
                backtracking(i + 1, r, g + 1, result + [(row, col, 1)])
                visited[row][col] = False
            if r < R:
                visited[row][col] = True
                backtracking(i + 1, r + 1, g, result + [(row, col, -1)])
                visited[row][col] = False


# 2. 각 조합에 따라 배양액이 퍼지며 같은 시간에 같은 위치에 G,R이 만나는 지점 찾기
def bfs(arr):
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    q = deque(arr)
    flower = 0
    check = copy.deepcopy(board)

    for r, c, color in arr:
        check[r][c] = color

    while q:
        x, y, color = q.popleft()
        if check[x][y] == "F":
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if in_range(nx, ny):
                time = check[x][y] + color  # 시간 표시

                # 다음 좌표가 호수가 아니거나
                if check[nx][ny] == "O":
                    check[nx][ny] = time
                    q.append((nx, ny, color))
                # 꽃을 배양할 수 있다면
                elif isinstance(check[nx][ny], int) and check[nx][ny] + time == 0:
                    flower += 1
                    check[nx][ny] = "F"

    return flower


# 3. 최대 꽃 개수 찾기
backtracking(0, 0, 0, [])
print(answer)

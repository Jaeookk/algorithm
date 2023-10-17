# 시간 초과 코드
# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]

# direction = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
# answer = 0


# def check(x, y):
#     for i in range(4):
#         k = 1
#         while True:
#             nx, ny = x + direction[i][0] * k, y + direction[i][1] * k
#             if 0 <= nx < n and 0 <= ny < n:  # 이동 좌표가 범위 안에 있고
#                 if graph[nx][ny] == "B":  # 해당 좌표에 비숍이 있다면 False
#                     return False
#                 k += 1
#             else:
#                 break
#     return True


# def solve(count):
#     global answer
#     answer = max(answer, count)

#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] == 1:  # 비숍을 놓을 수 있다면
#                 # 대각선 방향에 다른 비숍이 없다면
#                 if check(i, j):
#                     graph[i][j] = "B"
#                     solve(i, j, count + 1)
#                     graph[i][j] = 1


# solve(0)
# print(answer)


# # python3 10348ms
# N = int(input())
# graph = [list(map(int, input().split())) for _ in range(N)]
# # 좌상향 대각 여부 확인 row-col+(n-1) -> idx
# left_upper = [0] * (2 * (N - 1) + 1)
# # 우상향 대각 여부 확인 row+col -> idx
# right_upper = [0] * (2 * (N - 1) + 1)

# answer = 0
# right_upper_list = dict()

# for diag in range(2 * (N - 1) + 1):
#     right_upper_list[diag] = []
#     for row in range(N):
#         if diag - row >= 0 and diag - row < N and graph[row][diag - row] == 1:
#             right_upper_list[diag].append((row, diag - row))
# n = len(right_upper_list)


# def dfs(num, cost):
#     global answer
#     flag = False
#     if num == n:
#         answer = max(cost, answer)
#         return
#     for row, col in right_upper_list[num]:  # 우상향 대각선 조사
#         # [num] 번째 우상향 대각선에 비숍이 없고
#         # [num] 번째 우상향 대각선에 포함된 각각의 좌표에 해당하는 좌상향 대각선에도 비숍이 없다면
#         # 해당 좌표에는 비숍을 추가할 수 있다.
#         if right_upper[num] != 1 and left_upper[row - col + (N - 1)] != 1:
#             right_upper[num] = 1
#             left_upper[row - col + (N - 1)] = 1
#             flag = True

#             dfs(num + 1, cost + 1)

#             right_upper[num] = 0
#             left_upper[row - col + (N - 1)] = 0

#     if not flag:  # 이번 우상향 대각선에서 어떠한 좌표에도 비숍을 넣지 않은 경우 << 시간초과 해결 방법!
#         dfs(num + 1, cost)


# dfs(0, 0)
# print(answer)


# python3 3604ms
in_range = lambda y, x: 0 <= y < n and 0 <= x < n

n = int(input())
board = [[] for _ in range(n)]
for i in range(n):
    board[i] = list(map(int, input().split()))

rd = {}  # 우하향(right down) 대각선
# (0,0)을 시작으로 하는 우하향 중앙을 기준으로 쁠마 (row,col) -> rd[col-row]
# 제일 왼쪽 아래가 -(n-1), 제일 오른쪽 위가 (n-1)
for i in range(-n + 1, n):
    rd[i] = 0  # 초기화


def upper_bound(diag):  # 현재 대각선(우상향) 위치에서부터 끝 대각선까지 뽑힐 가능성이 있는 애들의 갯수 반환
    able_rus = 0  # 가능한 우상향 대각선들의 개수, 실제 가능하다기보단 단순히 가능할수도 있는 애들
    for d in range(diag, 2 * n - 1):
        for row in range(d + 1):
            col = d - row
            if (
                in_range(row, col) and board[row][col] and rd[col - row] == 0
            ):  # 좌표가 범위를 벗어나지 않고, 비숍을 놓을수 있으며(값=1), 우하향 대각선에도 걸리지 않는다면
                able_rus += 1
                break
    return able_rus


def f(diag, cnt):  # diag 은 우상향 대각선의 번호. 첫 우상향 대각선이 0, 마지막이 2*n-2
    global ans
    if diag == 2 * n:
        ans = max(ans, cnt)
        return

    ub = upper_bound(diag)  # 상한, 이번 대각선부터 끝까지 갔을 때 최대로 더 가질 수 있는 값
    if ub + cnt <= ans:  # 현재 cnt 값과 앞으로 최대한 얻을 수 있는 값을 더해도 기존 ans 보다 작으면 <<< 이것이 핵심인듯....
        return  # 빠져나온다

    for row in range(diag + 1):  # 현재 대각선에서 가능한 row,col 조합 찾기
        col = diag - row  # 각 우상향 대각선에 해당하는 (row, col) 좌표
        if in_range(row, col) and board[row][col] and rd[col - row] == 0:
            rd[col - row] = 1  # 현재 (row,col) 좌표에 비숍 넣었으므로, (row,col)가 속한 우하향 대각선 체크
            f(diag + 1, cnt + 1)  # (row,col) 좌표에 비숍 넣었으므로 cnt+1 하고 다음 우상향 대각선으로 감(diag+1)
            rd[col - row] = 0

    f(diag + 1, cnt)  # 이번 우상향 대각선에서 어떠한 좌표에도 비숍 넣지 않은 경우(cnt 그대로)


ans = 0
f(0, 0)
print(ans)

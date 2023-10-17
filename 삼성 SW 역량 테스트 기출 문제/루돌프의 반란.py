N, M, P, C, D = map(int, input().split())  # 격자크기, 게임 턴수, 산타 수, 루돌프 힘, 산타 힘
rx, ry = map(int, input().split())
rx, ry = rx - 1, ry - 1

# santas = [list(map(int, input().split()))]
santas = [[0, -1, -1]]
board = [[0] * N for _ in range(N)]

for _ in range(P):
    sn, r, c = map(int, input().split())
    santas.append([sn, r - 1, c - 1])
    board[r - 1][c - 1] = sn

santas.sort(key=lambda x: x[0])
board[rx][ry] = 1001

is_stun = [0] * (P + 1)
is_out = [True] + [False] * (P)
score = [0] * (P + 1)


in_range = lambda x, y: 0 <= x < N and 0 <= y < N


def rudolf():
    global rx, ry
    # 가장 가까운 산타를 향해 1칸 돌진 (탈락하지 않은 산타를 선택)
    # 2명 이상이라면 r좌표가 큰 산타를 선택. 이마저도 같다면 c좌표가 큰 산타를 선택
    # 상하좌우 대각선 돌진 가능.
    # 즉, 가장 우선순위가 높은 산타를 향해 8방향 중 가장 가까워 지는 방향으로 한 칸 돌진
    dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

    temp = 100000

    for i in range(1, P + 1):
        if is_out[i]:
            continue
        santa_num, santa_x, santa_y = santas[i]
        distance = pow((rx - santa_x), 2) + pow((ry - santa_y), 2)

        if temp > distance:
            res = [(santa_num, santa_x, santa_y)]
            temp = distance
        elif temp == distance:
            res.append((santa_num, santa_x, santa_y))

    res.sort(key=lambda x: (-x[1], -x[2]))  # r좌표가 크고, c좌표가 큰 산타 선택

    close_santa, close_x, close_y = res[0]  # 가장 가까운 산타, 좌표

    temp = 100000
    for i in range(8):
        nrx, nry = rx + dx[i], ry + dy[i]
        if in_range(nrx, nry):
            distance = pow((nrx - close_x), 2) + pow((nry - close_y), 2)
            if distance < temp:
                next_rx, next_ry = nrx, nry
                rdx, rdy = dx[i], dy[i]
                temp = distance

    rx, ry = next_rx, next_ry
    return rdx, rdy
    # return next_rx, next_ry  # 루돌프가 움직일 좌표


def santa(santa_num, santa_x, santa_y):
    """
    산타의 현 좌표를 입력받아 다음 좌표를 구함.
    단, 이전에 산타가 기절인지 아웃인지 확인하고 함수를 실행해야 한다!!!
    """
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # 상우하좌
    sdx, sdy = 0, 0
    next_sx, next_sy = santa_x, santa_y
    temp = pow((rx - santa_x), 2) + pow((ry - santa_y), 2)

    for i in range(4):
        nx, ny = santa_x + dx[i], santa_y + dy[i]
        # 움직일 수 있는 지 확인하는 코드 넣어야함!!!!!!
        if in_range(nx, ny) and (board[nx][ny] == 0 or board[nx][ny] == 1001):
            distance = pow((rx - nx), 2) + pow((ry - ny), 2)
            if distance < temp:
                next_sx, next_sy = nx, ny
                sdx, sdy = dx[i], dy[i]
                temp = distance

    santas[santa_num] = [santa_num, next_sx, next_sy]

    return sdx, sdy


def conflict(santa_num, dx, dy, who):
    # 루돌프가 움직여서 부딪히면 산타는 루돌프 이동 방향대로 C 날아감
    if who == "R":
        scx, scy = rx + dx * C, ry + dy * C
        score[santa_num] += C
    # 산타가 움직여서 부딪히면 산타는 산타 이동 방향 반대로 D 날아감
    else:
        dx, dy = -dx, -dy
        scx, scy = rx + dx * D, ry + dy * D
        score[santa_num] += D

    if not in_range(scx, scy):
        is_out[santa_num] = True
        santas[santa_num] = [santa_num, -1, -1]
    else:
        santas[santa_num] = [santa_num, scx, scy]
        is_stun[santa_num] = 2

        while board[scx][scy] != 0 and board[scx][scy] != santa_num:  # 튕겨나간 곳에 다른 산타가 있다면
            santa_num = board[scx][scy]
            scx, scy = scx + dx, scy + dy  # 다른 산타가 튕겨나간 좌표
            if not in_range(scx, scy):  # 아웃 되는지 확인
                is_out[santa_num] = True
                santas[santa_num] = [santa_num, -1, -1]
                break
            santas[santa_num] = [santa_num, scx, scy]  # 아웃이 아니라면 다른 산타의 좌표 최신화


# 게임판 최신화
def create_board():
    temp = [[0] * N for _ in range(N)]
    temp[rx][ry] = 1001

    for k in range(1, len(santas)):
        if in_range(santas[k][1], santas[k][2]):
            temp[santas[k][1]][santas[k][2]] = k

    return temp


for game in range(M):
    for l in range(1, P + 1):
        if is_stun[l] > 0:
            is_stun[l] = is_stun[l] - 1

    # 루돌프
    rudolf_dx, rudolf_dy = rudolf()
    # next_rx, next_ry = rudolf()

    # 충돌 및 상호작용
    if 0 < board[rx][ry] <= 1000:
        s_num = board[rx][ry]
        sx, sy = santas[s_num][1:]
        conflict(s_num, rudolf_dx, rudolf_dy, "R")
    board = create_board()

    # 산타
    for idx in range(1, P + 1):
        s_num, sx, sy = santas[idx]
        if is_stun[s_num] > 0:
            continue
        if is_out[s_num]:
            continue

        santa_dx, santa_dy = santa(s_num, sx, sy)
        if santa_dx == 0 and santa_dy == 0:
            continue
        _, santa_new_x, santa_new_y = santas[s_num]

        if board[santa_new_x][santa_new_y] == 1001:
            conflict(s_num, santa_dx, santa_dy, "S")
        board = create_board()

    flag = True
    for j in range(1, P + 1):
        if not is_out[j]:
            score[j] += 1
            flag = False

    if flag:  # 모든 산타가 아웃이라면 게임 종료
        break

print(*score[1:])

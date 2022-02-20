def UP(x, y):  # x:column, y:row
    Y = y - 1
    if 0 <= Y:
        if board[Y][x] > 0:
            if board[Y][x] == board[y][x]:
                board[Y][x] = board[y][x] * 2
                board[y][x] = -1  # Y행과 Y+1행이 합쳐지면 Y+1행은 -1로 표시
                return
            else:
                return
        elif board[Y][x] == -1:  # Y-1 row의 값은 이미 합쳐진 값
            board[Y][x] = board[y][x]  # Y행과 Y+1행 값을 바꾸고
            board[y][x] = 0  # Y+1행을 0으로 만듦.
            return
        else:  # Y행 x열의 값이 0이면
            board[Y][x] = board[y][x]  # Y행에 Y+1행의 값을 넣고
            board[y][x] = 0  # Y+1행은 0으로 만들고
            UP(x, Y)  # Y-1행과 Y행의 값이 합쳐질 수도 있으니 다시 함수 호출


def Down(x, y):
    Y = y + 1
    if Y < N:
        if board[Y][x] > 0:
            if board[Y][x] == board[y][x]:
                board[Y][x] = board[y][x] * 2
                board[y][x] = -1
                return
            else:
                return

        elif board[Y][x] == -1:
            board[Y][x] = board[y][x]
            board[y][x] = 0
            return
        else:
            board[Y][x] = board[y][x]
            board[y][x] = 0
            Down(x, Y)


def Right(x, y):
    X = x + 1
    if X < N:
        if board[y][X] > 0:
            if board[y][X] == board[y][x]:
                board[y][X] = board[y][x] * 2
                board[y][x] = -1
                return
            else:
                return

        elif board[y][X] == -1:
            board[y][X] = board[y][x]
            board[y][x] = 0
            return
        else:
            board[y][X] = board[y][x]
            board[y][x] = 0
            Right(X, y)


def Left(x, y):
    X = x - 1
    if 0 <= X:
        if board[y][X] > 0:
            if board[y][X] == board[y][x]:
                board[y][X] = board[y][x] * 2
                board[y][x] = -1
                return
            else:
                return

        elif board[y][X] == -1:
            board[y][X] = board[y][x]
            board[y][x] = 0
            return
        else:
            board[y][X] = board[y][x]
            board[y][x] = 0
            Left(X, y)


T = int(input())

for test_case in range(1, T + 1):
    N, S = map(str, input().split())
    N = int(N)
    board = []
    for n in range(N):
        board.append(list(map(int, input().split())))

    if S == "up":
        for y in range(N):  # y : row
            for x in range(N):  # x : column
                if board[y][x]:  # y행 x열 값이 양의 정수이면
                    UP(x, y)
    if S == "down":
        for y in range(N - 1, -1, -1):
            for x in range(N):
                if board[y][x]:
                    Down(x, y)
    if S == "right":
        for x in range(N - 1, -1, -1):
            for y in range(N):
                if board[y][x]:
                    Right(x, y)
    if S == "left":
        for x in range(N):
            for y in range(N):
                if board[y][x]:
                    Left(x, y)
    for y in range(N):
        for x in range(N):
            if board[y][x] == -1:
                board[y][x] = 0

    print(f"#{test_case}")
    for i in range(N):
        print(" ".join(map(str, board[i])))

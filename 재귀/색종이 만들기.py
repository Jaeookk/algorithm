n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

zero = 0
one = 0


def func(x, y, n):
    global zero, one
    init = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != init:
                for k in range(2):
                    for l in range(2):
                        func(x + k * n // 2, y + l * n // 2, n // 2)
                return

    if init == 0:
        zero += 1
    elif init == 1:
        one += 1
    return


func(0, 0, n)
print(zero)
print(one)

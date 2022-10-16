n = int(input())
board = [list(map(int, input())) for _ in range(n)]

result = ""


def func(x, y, n):
    """
    x : 행 위치
    y : 열 위치
    n : 정사각형 길이
    """
    global result
    init = board[x][y]

    # 종이가 모두 같은 수로 이루어져 있는지 확인
    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != init:
                # 같은 수로 이루어져 있지 않다면, 4 등분을 합시다.
                result += "("  # 사각형을 4등분 해야하므로 "(" 추가.
                for k in range(2):
                    for l in range(2):
                        func(x + k * n // 2, y + l * n // 2, n // 2)
                result += ")"  # 4등분한 사각형을 모두 조사했으므로 ")"로 닫음.
                return

    if init == 0:
        result += "0"
    elif init == 1:
        result += "1"
    return


func(0, 0, n)
print(result)

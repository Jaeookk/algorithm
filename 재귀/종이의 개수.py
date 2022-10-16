N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
zero = 0
one = 0
minus_one = 0


def solve(x, y, n):
    """
    x : 행
    y : 열
    n : 정사각형 길이(n = 3^k)
    """
    global zero, one, minus_one
    # 종이가 모두 같은 수로 이루어져 있는지 확인
    init = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != init:
                # 같은 수로 이루어져 있지 않다면, 9 등분을 합시다.
                for k in range(3):
                    for l in range(3):
                        # 9등분을 하여 각 정사각형의 왼쪽위부터 탐색.
                        # 행 위치 : 기존 시작점(x) + 사각형을 3등분 하고 각 사각형의 시작 행(0,1,2 * (n//3))
                        solve(x + k * n // 3, y + l * n // 3, n // 3)
                # 같지 않기 때문에, 이 loop는 종료해줍니다. 불필요한 반복을 하지 않습니다.
                return
    if init == 0:
        zero += 1
    elif init == 1:
        one += 1
    elif init == -1:
        minus_one += 1
    return


solve(0, 0, N)

print(minus_one)
print(zero)
print(one)

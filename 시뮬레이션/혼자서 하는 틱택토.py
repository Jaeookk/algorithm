# https://school.programmers.co.kr/learn/courses/30/lessons/160585?language=python3C
def solution(board):
    check = {"O": 0, "X": 0}
    flag = {"O": False, "X": False}
    dir = [(-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1), (1, 0), (0, 1), (1, 1)]

    for r in range(3):
        for c in range(3):
            if board[r][c] != ".":
                target = board[r][c]
                check[target] += 1
                for d in dir:
                    temp = [False, False]
                    for i in range(1, 3):
                        dx = r + d[0] * i
                        dy = c + d[1] * i
                        if dx < 0 or dx > 2 or dy < 0 or dy > 2:
                            break
                        if board[dx][dy] == target:
                            temp[i - 1] = True
                    if temp[0] and temp[1]:
                        flag[target] = True

    if check["X"] > check["O"] or check["O"] - check["X"] > 1:
        return 0
    if flag["O"] == True and flag["X"] == True:
        return 0
    if flag["O"] == True and check["O"] <= check["X"]:
        return 0
    if flag["X"] == True and check["O"] != check["X"]:
        return 0

    return 1

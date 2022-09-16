# https://school.programmers.co.kr/learn/courses/30/lessons/77485
def solution(rows, columns, queries):
    answer = []
    array = [[i * columns + j for j in range(1, columns + 1)] for i in range(rows)]

    for x1, y1, x2, y2 in queries:
        tmp = array[x1 - 1][y1 - 1]
        mini = tmp

        for k in range(x1 - 1, x2 - 1):  # 왼쪽 세로
            test = array[k + 1][y1 - 1]
            array[k][y1 - 1] = test
            mini = min(mini, test)

        for k in range(y1 - 1, y2 - 1):  # 아래 가로
            test = array[x2 - 1][k + 1]
            array[x2 - 1][k] = test
            mini = min(mini, test)

        for k in range(x2 - 1, x1 - 1, -1):  # 오른쪽 세로
            test = array[k - 1][y2 - 1]
            array[k][y2 - 1] = test
            mini = min(mini, test)

        for k in range(y2 - 1, y1 - 1, -1):  # 위쪽 가로
            test = array[x1 - 1][k - 1]
            array[x1 - 1][k] = test
            mini = min(mini, test)

        array[x1 - 1][y1] = tmp
        answer.append(mini)

    return answer

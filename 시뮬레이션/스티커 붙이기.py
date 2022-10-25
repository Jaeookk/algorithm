import sys


def rotation(sticker):
    r, c = len(sticker), len(sticker[0])
    temp = [[0 for _ in range(r)] for _ in range(c)]
    for i in range(r):
        for j in range(c):
            temp[j][r - i - 1] = sticker[i][j]
    return len(temp), len(temp[0]), temp


def check(sticker, graph, x, y):
    r, c = len(sticker), len(sticker[0])
    for i in range(x, x + r):
        for j in range(y, y + c):
            if sticker[i - x][j - y] == 1:
                if graph[i][j] != 0:
                    return False
    return True


def attach(x, y, sticker):
    r, c = len(sticker), len(sticker[0])
    for i in range(x, x + r):
        for j in range(y, y + c):
            if sticker[i - x][j - y] == 1:
                notebook[i][j] = 1


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    notebook = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        r, c = map(int, input().split())
        sticker = [list(map(int, input().split())) for _ in range(r)]
        count = 0

        while count < 4:

            if n < r or m < c:
                r, c, sticker = rotation(sticker)
                count += 1
                continue

            flag = False
            for i in range(n - r + 1):
                for j in range(m - c + 1):
                    if not check(sticker, notebook, i, j):
                        continue
                    attach(i, j, sticker)
                    flag = True
                    break
                if flag:
                    break

            if flag == True:
                break
            else:
                r, c, sticker = rotation(sticker)
                count += 1

    result = 0
    for i in range(n):
        for j in range(m):
            if notebook[i][j] == 1:
                result += 1
    print(result)

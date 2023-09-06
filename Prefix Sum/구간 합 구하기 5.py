import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

psum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        # psum[i][j] = i행 j열 까지의 모든 값의 합
        psum[i + 1][j + 1] = arr[i][j] + psum[i][j + 1] + psum[i + 1][j] - psum[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    ret = psum[x2][y2] - psum[x1 - 1][y2] - psum[x2][y1 - 1] + psum[x1 - 1][y1 - 1]
    print(ret)

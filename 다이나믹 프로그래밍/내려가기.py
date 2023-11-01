import sys

input = sys.stdin.readline
n = int(input())


dp_M = [[0, 0, 0] for _ in range(2)]
dp_m = [[0, 0, 0] for _ in range(2)]

for i in range(n):
    t = i % 2
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            dp_M[t][0] = max(dp_M[t - 1][0], dp_M[t - 1][1]) + a
            dp_m[t][0] = min(dp_m[t - 1][0], dp_m[t - 1][1]) + a
        elif j == 1:
            dp_M[t][1] = max(dp_M[t - 1]) + b
            dp_m[t][1] = min(dp_m[t - 1]) + b
        else:
            dp_M[t][2] = max(dp_M[t - 1][1], dp_M[t - 1][2]) + c
            dp_m[t][2] = min(dp_m[t - 1][1], dp_m[t - 1][2]) + c

print(max(dp_M[n % 2 - 1]), min(dp_m[n % 2 - 1]))

# 바텀업 방식
dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
for i in range(21):
    for j in range(21):
        for k in range(21):
            if i <= 0 or j <= 0 or k <= 0:
                dp[i][j][k] = 1
            elif i < j and j < k:
                dp[i][j][k] = dp[i][j][k - 1] + dp[i][j - 1][k - 1] - dp[i][j - 1][k]
            else:
                dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] - dp[i - 1][j - 1][k - 1]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    if a <= 0 or b <= 0 or c <= 0:
        print(f"w({a}, {b}, {c}) = 1")
        continue
    elif a > 20 or b > 20 or c > 20:
        print(f"w({a}, {b}, {c}) = {dp[-1][-1][-1]}")
    else:
        print(f"w({a}, {b}, {c}) = {dp[a][b][c]}")


# 탑다운방식
# def w(a, b, c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return 1
#     elif a > 20 or b > 20 or c > 20:
#         return w(20, 20, 20)

#     elif stg[a][b][c] != 0:
#         return stg[a][b][c]

#     elif a < b and b < c:
#         stg[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
#         return stg[a][b][c]
#     else:
#         stg[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + \
#             w(a-1, b, c-1) - w(a-1, b-1, c-1)
#         return stg[a][b][c]


# result = []
# stg = [[[0]*(21) for _ in range(21)] for _ in range(21)]
# i = 0

# while i == 0:
#     a, b, c = map(int, input().split())
#     if a == -1 and b == -1 and c == -1:
#         i = 1
#     else:
#         print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
# print(*result, sep='\n')

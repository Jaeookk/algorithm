# 앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 한다.
# 길이가 1인 경우 자기자신인 경우 1
# 길이가 2인 경우 바로 옆 인덱스의 수와 같을 경우 1
# 길이가 3 이상인 경우 양 끝(s와e)이 같은 수이고 그 사이 숫자(dp[s+1][e-1])가 1이면(팰린드롬이면) 1
# dp[i][j] = i~j 인덱스의 수가 팰린드롬인지 여부

import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):  # 길이가 1인 경우
    dp[i][i] = 1

for i in range(n - 1):  # 길이가 2인 경우(e-s = 1)
    if array[i] == array[i + 1]:
        dp[i][i + 1] = 1

# s와 e의 간격이 0,1인 경우는 이미 조사를 했으므로, 간격이 2인 경우부터 조사
# 이때, 간격이 2일때 (121과 같이) 양끝이 같은지 조사하고, 양끝을 제외한 가운데 숫자가 팰린드롬인지 검사하는데
# 가운데 숫자는 길이가 0인 경우로서 이미 조사를 했기 때문에, dp 최신화 가능.

for i in range(2, n):  # e-s >= 2
    for j in range(n - i):  # j는 시작점(s)
        if array[j] == array[i + j] and dp[j + 1][i + j - 1] == 1:
            # 처음과 끝이 같고, j+1 ~ i+j-1 이 팰린드롬이면
            dp[j][i + j] = 1  # j ~ i+j도 팰린드롬.

m = int(input())
question = []
for _ in range(m):
    a, b = map(int, input().split())
    print(dp[a - 1][b - 1])

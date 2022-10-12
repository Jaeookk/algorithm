# dp[i][j] = S1[:i]와 S2[:j]를 비교했을 때 가장 긴 부분 수열의 길이
# 점화식
# dp[i][j] = max(dp[i-1][j], dp[i][j-1]) , if S1[i] != S2[j] 알파벳이 다르면 이전까지 비교한 값중 최대값
# dp[i][j] = dp[i-1][j-1] + 1 , 알파벳이 같은 경우 S1,S2의 각 글자가 추가되기 이전의 길이 + 1

#   0 A C A Y K P
# 0 0 0 0 0 0 0 0
# C 0 0 1 1 1 1 1
# A 0 1 1 2 2 2 2
# P 0 1 1 2 2 2 3
# C 0 1 2 2 2 2 3
# A 0 1 2 3 3 3 3
# K 0 1 2 3 3 4 4

S1 = input()
S2 = input()

dp = [[0] * (len(S2) + 1) for _ in range(len(S1) + 1)]
for i in range(1, len(S1) + 1):
    for j in range(1, len(S2) + 1):
        if S1[i - 1] == S2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp)
print(max(dp[-1]))

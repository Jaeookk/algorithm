# https://school.programmers.co.kr/learn/courses/30/lessons/12904#
def solution(s):
    answer = 1
    l = len(s)
    dp = [[0 for _ in range(l)] for _ in range(l)]  # dp[i][j] = i~j 인덱스의 요소가 팰린드롬인지 여부

    # 길이가 1 인 경우 => 팰린드롬
    for i in range(l):
        dp[i][i] = 1

    # 길이가 2인 경우
    for i in range(l - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 1
    # 간격이 0,1인 경우는 이미 조사를 했으므로, 간격이 2인 경우(길이가 3)부터 조사
    # 이때, 간격이 2일때 (121과 같이) 양끝이 같은지 조사하고, 양끝을 제외한 가운데 숫자가 팰린드롬인지 검사하는데
    # 가운데 숫자는 길이가 0인 경우로서 이미 조사를 했기 때문에, dp 최신화 가능.

    for interval in range(2, l):
        for start in range(l - interval):
            if s[start] == s[start + interval] and dp[start + 1][start + interval - 1] == 1:
                # 양 끝이 같고, 그 사이의 요소가 팰린드롬이면
                dp[start][start + interval] = 1
                answer = max(answer, interval + 1)

    return answer

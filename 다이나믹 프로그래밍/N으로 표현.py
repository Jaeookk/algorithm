# https://school.programmers.co.kr/learn/courses/30/lessons/42895#


def solution(N, number):
    answer = 0
    dp = [set([int(str(N) * i)]) for i in range(1, 10)]
    # 점화식
    # dp[n] = (N을 k개 사용해서 나타낼 수 있는 수) (+)or(-)or(x)or(÷) (N을 n-k개 사용해서 나타낼 수 있는 수)
    # 단, 1 <= k < n

    # N 사용 횟수
    for n in range(8):
        for k in range(n):
            # k개
            for a in dp[k]:
                # n-k개
                for b in dp[n - k - 1]:
                    dp[n].add(a + b)
                    dp[n].add(a - b)
                    dp[n].add(a * b)
                    if b != 0:
                        dp[n].add(a // b)
        if number in dp[n]:
            return n + 1
    return -1

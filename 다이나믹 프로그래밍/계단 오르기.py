# 1. 테이블 정의하기
# d[i][j] = 현재까지 j개의 계단을 연속해서 밟고, i번째 계단까지 올라섰을 때 점수 합의 최댓값,
# 단 i번째 계단은 반드시 밟아야함. -> j는 1 or 2
# 2. 점화식 찾기
# d[k][1] = k번째 계단을 밟았을때 연속되는 첫번째 계단이므로
#           k-2번째 계단을 밟고 2계단 건너뛰어 k번째 계단을 밟았다는 의미
# 즉, d[k][1] = max(d[k-2][1], d[k-2][2]) + s[k] (s[k]는 k번째 계단의 점수)

# d[k][2] = d[k-1][1] + s[k]
# 3. 초기값 정하기
# d[1][1] = s[1], d[1][2] = 0
# d[2][1] = s[2], d[2][2] = s[1] + s[2]

n = int(input())
scores = [0] + [int(input()) for _ in range(n)]
d = [[0] * 3 for _ in range(n + 1)]


def main():
    if n == 1:
        print(scores[1])
        return
    d[1][1] = scores[1]
    d[1][2] = 0
    d[2][1] = scores[2]
    d[2][2] = scores[1] + scores[2]

    for i in range(3, n + 1):
        d[i][1] = max(d[i - 2][1], d[i - 2][2]) + scores[i]
        d[i][2] = d[i - 1][1] + scores[i]

    print(max(d[n]))


# # 1차원 dp 풀이 방법
# N = int(input())
# stair = [0] * 301
# for i in range(N):
#     stair[i] = int(input())

# def main():
#     DP = [0] * 301
#     DP[0] = stair[0]
#     DP[1] = stair[0] + stair[1]
#     DP[2] = max(stair[0] + stair[2], stair[1] + stair[2])

#     for i in range(3, N):
#         DP[i] = max(DP[i - 3] + stair[i - 1] + stair[i], DP[i - 2] + stair[i])

#     print(DP[N - 1])

if __name__ == "__main__":
    main()

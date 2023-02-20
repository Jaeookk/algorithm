# dp[0][row][col] = 가로 파이프에 대한 dp
# dp[1][row][col] = 대각선 파이프에 대한 dp
# dp[2][row][col] = 세로 파이프에 대한 dp
# 해당 값은 그 칸(row, col)을 끝으로 하는 (가로, 세로, 대각선) 파이프의 개수

# 가로로 올 수 있는 경우의 수 -> (가로->가로, 대각선->가로) 이 경우의 수들의 합
# 세로로 올 수 있는 경우의 수 -> (세로->세로, 대각선->세로) 이 경우의 수들의 합
# 대각선으로 올 수 있는 경우의 수 -> (가로->대각선 가능, 세로->대각선, 대각선->대각선) 이 경우의 수들의 합


def solution(n):
    global dp
    for i in range(2, n):
        if graph[0][i] == 1:
            break
        dp[0][0][i] = dp[0][0][i - 1]  # (0,i)를 끝으로 하는 가로 파이프 수는 (0, i-1)과 같음

    for i in range(1, n):
        for j in range(1, n):
            # (i,j)를 기준으로 위,왼쪽, 1시방향이 모두 벽이 아니라면
            if graph[i][j] == 0 and graph[i][j - 1] == 0 and graph[i - 1][j] == 0:
                # (i,j)일때 대각선 파이프의 경우의수 추가
                dp[1][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]

            if graph[i][j] == 0:
                dp[0][i][j] = dp[0][i][j - 1] + dp[1][i][j - 1]
                dp[2][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]
    return dp


if __name__ == "__main__":
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
    dp[0][0][1] = 1

    solution(n)
    print(sum(dp[i][n - 1][n - 1] for i in range(3)))

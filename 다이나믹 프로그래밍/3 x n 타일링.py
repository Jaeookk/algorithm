# https://school.programmers.co.kr/learn/courses/30/lessons/12902
def solution(n):
    # 홀수인 경우는 0개이다.
    # n=2인 경우 3가지 경우의 타일 모양이 나오고, 그 다음 단계로 진행할 때마다 매번 2개씩 새로운 모양의 타일이 생긴다.
    answer = 0
    dp = [0]*(n+1)
    if n < 2:
        return dp[n]
    dp[2] = 3
    
    # 점화식 : dp[n] = dp[n-2]*3 + dp[n-4]*2 + d[n-6]*2 + ... + dp[2]*2 + 2
    for i in range(4,len(dp),2):
        dp[i] = (dp[i-2]*3 + sum(dp[:i-3])*2+2)%1000000007
        
    return dp[n]

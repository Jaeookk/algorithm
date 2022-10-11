# 동전이 오름차순으로 정렬되어 주어지기 때문에 작은 동전부터 해당 동전을 이용하여
# m 원을 만들 수 있는 경우의 수를 더한 뒤, 다음 동전으로 넘어가서 이전 경우의 수에
# 해당 동전으로 만들 수 있는 경우의 수를 순차적으로 더해가며 답을 구한다.

# dp[i] = i원을 만들 수 있는 경우의 수
# ex) coins = [1, 3, 10] , M = 10
# 1. 1원짜리 동전으로 1~10원까지 각 경우의 수를 구함.
# 2. 3원짜리 동전으로 1~10원까지 각 경우의 수를 구하여 더함
# 2.1 이때 만약 4원을 만들고 싶다 -> 1원을 만드는 경우의 수 + 3원
# 2.2 만약 7원을 만들고 싶다 -> 4원을 만드는 경우의 수 + 3원
# 즉, 점화식 : dp[i] += dp[i - coin]

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [0] * (M + 1)
    dp[0] = 1

    for coin in coins:  # 가장 작은 동전부터 경우의수 구하기
        for i in range(1, M + 1):
            if i < coin:
                continue
            dp[i] += dp[i - coin]
    print(dp[M])

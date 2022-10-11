# d[i] = i명일 때 좌석에 앉는 서로 다른 방법의 가짓수
# d[i] = d[i-1] + d[i-2]

# 하지만 여기서 중요한 점은 고정석을 기준으로 나뉘는 그룹의 가짓수를 서로 곱하면 된다.
# 예를들어 4,7이 고정석이면
# (1,2,3) (5,6) (8,9) 이렇게 3개의 그룹이 나오고
# 좌석에 앉는 가짓수는 각각의 그룹의 가짓수를 곱하면 된다.

n = int(input())
m = int(input())

vip = [int(input()) for _ in range(m)]

dp = [1] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

result = 1
if m == 0:
    result = dp[n]
else:
    temp = 0
    for v in vip:
        result *= dp[v - temp - 1]
        temp = v
    # 나머지 곱하기
    result *= dp[n - temp]
print(result)

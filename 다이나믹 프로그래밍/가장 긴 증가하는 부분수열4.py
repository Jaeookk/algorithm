a = int(input())

array = list(map(int, input().split()))

dp = [1] * a
result = []
for i in range(1, a):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

result = []
x = max(dp)

for i in range(a - 1, -1, -1):
    if dp[i] == x:
        result.append(array[i])
        x -= 1
result.reverse()
print(max(dp))
for i in result:
    print(i, end=" ")

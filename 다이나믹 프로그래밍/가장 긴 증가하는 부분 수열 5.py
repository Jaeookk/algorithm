# https://seohyun0120.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4LIS-%EC%99%84%EC%A0%84-%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import bisect
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]
record = []  # 각 인덱스별 그때의 LIS의 값을 저장.

for i in range(n):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
        # dp의 길이가 i일때의 LIS 값이므로
        record.append(len(dp))
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]
        # arr[i]가 가장 클 때의 LIS의 값이 idx
        record.append(idx + 1)

print(record)

result = []
x = len(dp)
for i in range(n - 1, -1, -1):
    if record[i] == x:
        result.append(arr[i])
        x -= 1
result.reverse()
print(len(dp))
print(*result)

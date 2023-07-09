# 백준 1107 골드4
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
ans = abs(100 - n)

if m != 0:
    broken = set(input().split())
else:
    broken = set()

# 작은 수 -> 큰 수: 0 ~ 500000, 큰 수 -> 작은 수: 500001 ~ 1000000
for channel in range(1000001):
    for i in str(channel):
        if i in broken:  # 해당 숫자 버튼이 고장난 경우
            break
    else:  # 채널을 누른 후 +/- 버튼으로 n까지 가기
        ans = min(ans, len(str(channel)) + abs(channel - n))  # min(기존답, 숫자 버튼 클릭 수 + '+/-' 버튼 클릭 수)

print(ans)

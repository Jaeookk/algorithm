# 1. 테이블 정의하기
# d[i] = i를 1,2,3의 합으로 나타내는 방법의 수
# 2. 점화식 찾기
# d[4] = ?
# 1+1+1+1, 3+1, 2+1+1, 1+2+1 (3을 1,2,3의 합으로 나타내는 방법)+1 -> d[3]
# 1+1+2, 2+2 (2를 1,2,3의 합으로 나타내는 방법)+2 -> d[2]
# 1+3 (1을 1,2,3의 합으로 나타내는 방법)+3 -> d[1]
# ----d[i] = d[i-1]+d[i-2]+d[i-3]----
import sys

sys.setrecursionlimit(10000001)
n = int(sys.stdin.readline())
d = [0] * 10000001
d[1] = 1
d[2] = 2
d[3] = 4

for _ in range(n):
    x = int(input())
    if x < 4:
        print(d[x])
        continue
    for i in range(4, x + 1):
        d[i] = (d[i - 1] + d[i - 2] + d[i - 3]) % 1000000009
    print(d[x])

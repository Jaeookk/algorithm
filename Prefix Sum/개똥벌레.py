import sys

input = sys.stdin.readline
n, h = map(int, input().split())


up = [0] * (h + 1)  # 석순
down = [0] * (h + 1)  # 종유석

for i in range(n):
    if i % 2 == 0:
        up[int(input())] += 1
    else:
        down[h - int(input()) + 1] += 1

for i in range(h - 1, 0, -1):  # 꼭대기에서 뿌리로로 흝으면서 h구간에는 장애물이 몇 개 있는지 누적합으로 구하기
    up[i] += up[i + 1]
    down[h - i + 1] += down[h - i]

# print(up)
# print(down)

min_hurdle = n
count = 0

for i in range(1, h + 1):  # 구간을 아래서부터 차례대로 살펴보기
    if min_hurdle > (up[i] + down[i]):  # i번째 구간에 있는 장애물 개수가 가장 작다면 최신화
        min_hurdle = up[i] + down[i]
        count = 1
    elif min_hurdle == up[i] + down[i]:
        count += 1

print(min_hurdle, count)

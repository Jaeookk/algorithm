import sys

input = sys.stdin.readline
n = int(input())

line = []
h = []
for _ in range(n):
    a, b = map(int, input().split())
    line.append((a, b))
line.sort()

start = line[0][0]
end = line[0][1]
result = 0

for i in range(1, n):
    # 겹치는 경우
    if line[i][0] <= end < line[i][1]:
        end = max(end, line[i][1])

    # 겹치지 않는 경우
    elif line[i][0] > end:
        result += end - start
        start = line[i][0]
        end = line[i][1]

result += end - start
print(result)

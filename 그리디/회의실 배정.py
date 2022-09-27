N = int(input())

data = []
for i in range(N):
    a, b = map(int, input().split())
    data.append((a, b))
data.sort(key=lambda x: (x[1], x[0]))
# 끝나는 시간이 같다면, 시작하는 시간을 빠른 순으로 정렬을 하는 이유
# 만약에 정렬이 시작시간에 전혀 관계없이, 종료시간으로만 정렬되게 된다면, 문제가 생기게 됩니다.

# 1 3
# 8 8
# 4 8
# 이라는 예시에 대해서, 종료시간으로만 정렬하면, 위와 같이 정렬될 수도 있습니다.
# 그럴 때, 1 3과 8 8만 세므로 2가 나와서 오답이 됩니다.

# 실제로는 1~3시 1번, 4~8시 2번, 8~8시 3번으로 총 3개가 나와야합니다

result = []
result.append(data[0])

for i in range(1, len(data)):
    if data[i][0] >= result[-1][1]:
        result.append(data[i])
print(len(result))

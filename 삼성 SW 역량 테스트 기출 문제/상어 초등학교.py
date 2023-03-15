# BOJ 20608
import sys

input = sys.stdin.readline

n = int(input())
p = n * n
classroom = [[0] * n for _ in range(n)]
like_room = [[] for _ in range(p + 1)]  # 만족도 계산 시 필요
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(p):
    array = list(map(int, input().split()))
    student, like = array[0], array[1:]
    like_room[student] = like
    if p == 0:
        classroom[1][1] = array[0]
        continue
    rules = []
    for i in range(n):
        for j in range(n):
            sum_like, sum_empty = 0, 0
            if classroom[i][j] != 0:
                continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
                    continue
                if classroom[nx][ny] in like:
                    sum_like += 1
                if classroom[nx][ny] == 0:
                    sum_empty += 1
            rules.append((sum_like, sum_empty, (i, j)))
    rules.sort(key=lambda x: (-x[0], -x[1], x[2]))  # 규칙에 따라 정렬.

    classroom[rules[0][2][0]][rules[0][2][1]] = array[0]


# 만족도 계산
sum_answer = 0
for i in range(n):
    for j in range(n):
        answer = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
                continue
            if classroom[nx][ny] in like_room[classroom[i][j]]:  # 인접한 칸에 앉은 좋아하는 학생 수 구하기
                answer += 1
                continue
        if answer != 0:
            sum_answer += 10 ** (answer - 1)


print(sum_answer)

# https://level.goorm.io/exam/175194/%EA%B5%AC%EB%A6%84-%EC%8A%A4%ED%80%98%EC%96%B4/quiz/1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1])

answer = 1
start, end = arr[0]
temp = end
for start, end in arr:
    if temp < start:
        answer += 1
        temp = end
    temp = min(temp, end)
print(answer)

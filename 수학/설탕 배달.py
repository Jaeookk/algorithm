N = int(input())
answer = 0

while N >= 0:
    if N % 5 == 0:
        answer += int(N // 5)
        print(answer)
        break
    N -= 3
    answer += 1

if N < 0:
    print(-1)

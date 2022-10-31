n = int(input())
arr = list(map(int, input().split()))

answer = 0
for x in arr:
    if x == 1:
        continue
    elif x < 4:
        answer += 1
    else:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                # 소수가 아님
                break
        else:
            answer += 1
print(answer)

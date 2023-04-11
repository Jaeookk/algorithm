n = int(input())

d = [0] * (n + 1)
history = [i for i in range(n + 1)] # history[i] 의 값은 i를 문제에서 주어진 3가지 연산 중 하나를 했을 때의 결과값
history[1] = 0

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    history[i] = i - 1

    if i % 3 == 0 and d[i] > d[i // 3] + 1:
        d[i] = d[i // 3] + 1
        history[i] = i // 3
    if i % 2 == 0 and d[i] > d[i // 2] + 1:
        d[i] = d[i // 2] + 1
        history[i] = i // 2

print(d[n])
print(n, end=" ")
while True:
    if history[n] == 0:
        break
    print(history[n], end=" ")
    n = history[n]

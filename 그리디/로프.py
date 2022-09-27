N = int(input())

ropes = []
for i in range(N):
    ropes.append(int(input()))
ropes.sort()

answer = 0
for i in range(N):
    answer = max(answer, (N - i) * ropes[i])
print(answer)

N = int(input())
arr = list(map(int, input().split()))

stack = []
answer = [0] * N

for i in range(N - 1, -1, -1):
    while stack and arr[stack[-1]] < arr[i]:
        idx = stack.pop()
        answer[idx] = i + 1

    stack.append(i)

print(*answer)

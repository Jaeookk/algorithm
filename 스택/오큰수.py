n = int(input())
arr = list(map(int, input().split()))

answer = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)


print(*answer)
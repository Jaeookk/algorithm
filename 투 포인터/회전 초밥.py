n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)] * 2

answer = 0
end = 0
stack = []
for start in range(len(arr) // 2):
    while end - start < k:
        stack.append(arr[end])
        end += 1
    test = set(stack)
    test.add(c)
    answer = max(answer, len(list(test)))
    stack.pop(0)

print(answer)

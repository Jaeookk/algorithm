# BOJ 2504
arr = input()
stack = []
cnt = 1
res = 0
for i in range(len(arr)):
    if arr[i] == "(":
        stack.append(arr[i])
        cnt *= 2
    elif arr[i] == "[":
        stack.append(arr[i])
        cnt *= 3
    elif arr[i] == ")":
        if stack == [] or stack[-1] == "[":
            print(0)
            break
        else:
            if arr[i - 1] == "(":
                res += cnt
            stack.pop()
            cnt //= 2
    elif arr[i] == "]":
        if stack == [] or stack[-1] == "(":
            print(0)
            break
        else:
            if arr[i - 1] == "[":
                res += cnt
            stack.pop()
            cnt //= 3
else:
    if stack:
        print(0)
    else:
        print(res)

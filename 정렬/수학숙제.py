m = int(input())
answer = []
for _ in range(m):
    arr = list(input())
    temp = ""
    for i in range(len(arr)):
        if not arr[i].isnumeric():
            if temp:
                answer.append(int(temp))
                temp = ""
        else:
            temp += arr[i]

    if temp:
        answer.append(int(temp))

print(*sorted(answer), sep="\n")

A, P = map(int, input().split())

arr = [A]

while True:
    result = 0
    for i in str(arr[-1]):
        result += int(i) ** P
    if result in arr:
        break
    arr.append(result)

print(arr.index(result))

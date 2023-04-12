import sys

n = int(sys.stdin.readline())
arr = [sys.stdin.readline().strip().split() for _ in range(n)]

count = set()
for i in range(n):
    if arr[i][1] == "enter":
        count.add(arr[i][0])
    else:
        count.remove(arr[i][0])

print(*sorted(count, reverse=True), sep="\n")

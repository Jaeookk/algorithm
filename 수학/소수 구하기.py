import math


m, n = map(int, input().split())
arr = [True] * (n + 1)
arr[1] = False

for i in range(1, int(math.sqrt(n)) + 1):
    if arr[i] == False:
        continue
    for j in range(i**2, len(arr), i):
        arr[j] = False

for i in range(m, len(arr)):
    if arr[i] == True:
        print(i)

from itertools import combinations

t = int(input())

for _ in range(t):
    n, *arr = map(int, input().split())
    answer = 0
    for a, b in combinations(arr, 2):
        if a < b:
            a, b = b, a
        while b: # 유클리드 호제법
            temp = a % b
            a, b = b, temp
        answer += a
    print(answer)

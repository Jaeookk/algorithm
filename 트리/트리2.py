# 백준 1068

import sys


def dfs(num, arr):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    count = 0

    dfs(k, arr)

    count = 0
    for i in range(len(arr)):
        if arr[i] != -2 and i not in arr:
            count += 1
    print(count)

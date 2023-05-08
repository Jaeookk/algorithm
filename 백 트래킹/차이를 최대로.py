# 백준 10819 실버2

import sys


def dfs(idx, depth, sum_):
    if depth == n:
        result["max"] = max(result["max"], sum_)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            sum_ += abs(arr[idx] - arr[i])
            dfs(i, depth + 1, sum_)
            visited[i] = False
            sum_ -= abs(arr[idx] - arr[i])


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))

    visited = [False] * n
    result = {"max": 0}

    for i in range(n):
        visited[i] = True
        dfs(i, 1, 0)
        visited[i] = False

    print(result["max"])

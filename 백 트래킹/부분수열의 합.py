import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0


def dfs(idx, total):
    global cnt

    if idx >= n:
        return

    total += arr[idx]

    if total == s:
        cnt += 1

    # 현재 arr[idx]를 선택한 경우의 가지
    dfs(idx + 1, total)

    # 현재 arr[idx]를 선택하지 않은 경우의 가지
    dfs(idx + 1, total - arr[idx])


dfs(0, 0)
print(cnt)

# BOJ 5567 실버2
import sys


def dfs(x, depth):
    global s
    if depth == 2:
        return
    for f in arr[x]:
        dfs(f, depth+1)
        s.add(f)

if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    m = int(input())
    arr = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
        
    s = set()
    dfs(1,0)
    if 1 in s:
        print(len(s) - 1)
    else:
        print(len(s))

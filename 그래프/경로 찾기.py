# BOJ 11403 실버1
import sys
from collections import deque


def bfs(node1):
    queue = deque()
    queue.append(node1)
    visited = [0 for _ in range(n)]

    while queue:
        q = queue.popleft()

        for node2 in range(n):
            if visited[node2] == 0 and graph[q][node2] == 1: # 
                queue.append(node2)
                visited[node2] = 1
                result[node1][node2] = 1


if __name__ == "__main__":
    input = sys.stdin.readline
    
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        bfs(i)
    
    for i in result:
        print(*i)
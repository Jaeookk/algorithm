# 프로그래머스 LV.3 가장 먼 노드
# https://school.programmers.co.kr/learn/courses/30/lessons/49189
# 다익스트라 로도 풀 수 있다 하더라...


from collections import deque


def bfs(graph, v, n):  # 간선 개수 최대 구하기
    q = deque()
    q.append((v, 0))
    visited = [False] * (n + 1)
    visited[1] = True

    MAX = 0  # 최대 간선 개수
    count = 0

    while q:
        cur = q.popleft()
        if MAX < cur[1]:
            MAX = cur[1]
            count = 1
        elif MAX == cur[1]:
            count += 1
        for next in graph[cur[0]]:
            if visited[next] == False:
                visited[next] = True
                q.append((next, cur[1] + 1))
    return count


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)

    return bfs(graph, 1, n)

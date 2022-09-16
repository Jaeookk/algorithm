# https://school.programmers.co.kr/learn/courses/30/lessons/86971
from collections import deque


def bfs(n, graph, del_line):
    visited = [False] * (n + 1)
    visited[del_line[0]] = True  # 시작 노드 방문 처리
    q = deque([del_line[0]])
    cnt = 1  # 시작 노드 카운트

    while q:
        x = q.popleft()
        for i in graph[x]:  # x와 연결된 모든 노드에 대해서
            if visited[i] or i == del_line[1]:  # 이미 방문했거나, 끊어지는 부분의 노드인 경우 방문하지 않고 패스.
                continue
            q.append(i)
            visited[i] = True
            cnt += 1

    return cnt


def solution(n, wires):
    answer = 101
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for wire in wires:
        cnt = bfs(n, graph, wire)  # wire에 있는 노드들의 연결을 끊었을 때 한쪽 영역의 노드 개수 구하기
        answer = min(answer, abs((n - cnt) - cnt))  # (n-cnt)는 다른 한쪽 영역의 노드 개수
    return answer

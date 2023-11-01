from collections import deque

# ### 위상정렬 사용 ###
# T = int(input())

# for _ in range(T):
#     n = int(input())
#     arr = list(map(int, input().split()))

#     graph = [[] for _ in range(n + 1)]
#     indegree = [0] * (n + 1)

#     for v in range(n):
#         e = arr[v]
#         graph[v + 1].append(e)
#         indegree[e] += 1

#     q = deque()
#     for i in range(1, n + 1):
#         if indegree[i] == 0:
#             q.append(i)

#     result = []

#     while q:
#         x = q.popleft()
#         result.append(x)
#         for node in graph[x]:
#             indegree[node] -= 1

#             if indegree[node] == 0:
#                 q.append(node)

#     print(len(result))


### dfs 사용 ###
def dfs(now):
    global result

    visited[now] = True
    cycle.append(now)  # 사이클을 이루는 팀을 확인하기 위함
    next = numbers[now]

    if visited[next]:  # 방문가능한 곳이 끝났는지
        if next in cycle:  # 사이클 가능 여부
            result += cycle[cycle.index(next) :]  # 마지막 팀원이 가리키는 침원이 첫 팀원이 되어 팀을 이룸
        return
    else:
        dfs(next)


for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N  # 방문 여부
    result = []

    for i in range(1, N + 1):
        if not visited[i]:  # 방문 안한 곳이라면
            cycle = []
            dfs(i)  # DFS 함수 돌림

    print(N - len(result))  # 팀에 없는 사람 수

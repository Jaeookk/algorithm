from collections import deque
import sys
# 그냥 input()을 쓰니 시간초과가 났음.
f = sys.stdin.readline

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)

queue = deque([x])
# visited를 0으로 초기화하면 if visited[next_node] == 0 부분에서 4 -> 1이 카운트됨.
# 문제 조건에서 자기 자신으로 가는 최단 거리는 무조건 0인데 이 경우에는 0이 아니게된다.
# 4 5 3 1
# 1 2
# 1 3
# 2 3
# 2 4
# 4 1
# 0으로 초기화할 경우에는 출력이 출발도시인 1이 나와서 틀리고, -1로 초기화할 경우 답이 없기 때문에 -1이 출력되어 정답.
visited = [-1] * (n + 1)
visited[x] = 0 # 출발 도시까지의 거리는 0으로 설정
while queue:
    now = queue.popleft()
    for next_node in graph[now]:
        if visited[next_node] == -1:
            queue.append(next_node)
            visited[next_node] = visited[now] + 1

if k in visited:
    for i in range(n + 1):
        if visited[i] == k:
            print(i)
else:
    print(-1)


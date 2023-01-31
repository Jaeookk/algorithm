from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())  # 편의점 개수 0 <= n <= 100
    home = tuple(map(int, input().split()))
    mart = []
    for _ in range(n):
        mart.append(tuple(map(int, input().split())))
    festival = tuple(map(int, input().split()))

    result = "sad"

    q = deque()
    q.append(home)
    visited = [home]

    while q:
        x, y = q.popleft()
        for i in range(len(mart)):  # 모든 편의점에 대하여
            if (
                abs(x - mart[i][0]) + abs(y - mart[i][1]) <= 1000
                and mart[i] not in visited
            ):  # 거리가 되는 편의점이고 방문하지 않은 편의점이라면 큐에 담기
                nx, ny = mart[i]
                q.append((nx, ny))
                visited.append((nx, ny))

        # 모든 편의점에 대한 조사가 끝난 이후, 현재 지점에서 페스티벌에 갈 수 있다면
        if abs(x - festival[0]) + abs(y - festival[1]) <= 1000:
            result = "happy"
            break

    print(result)

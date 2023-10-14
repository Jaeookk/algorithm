import sys
from collections import deque

INF = 10000000
si = sys.stdin.readline

# N, M, K := 행, 열, 턴 수
N, M, K = map(int, si().split())

# a := 지도의 정보
a = [list(map(int, si().split())) for _ in range(N)]

# isAttacked := 이번 턴에 공격과 관련이 있었는가?
# lastAttacked := 마지막에 공격한 턴은 언제인가?
lastAttack = [[0 for _ in range(M)] for _ in range(N)]


def attack(x, y, power):  # (x, y) 에 있는 포탑이 power만큼의 공격을 받는다.
    isAttacked[x][y] = True
    a[x][y] = max(0, a[x][y] - power)


def isFinish():  # 만약 종료 조건을 만족했다면 true return, O(NM)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if a[i][j] != 0:
                cnt += 1
    return cnt == 1


def select_attacker() -> tuple:  # 공격자를 선정하는 함수, O(NM)
    minV, maxT, minI, minJ = INF, -1, 0, 0
    for sum in range(N + M - 2, -1, -1):  # sum(행+열) 을 최대부터 최소까지 순회
        for j in range(M - 1, -1, -1):  # 같은 sum에 대해서는 높은 열부터 탐색
            i = sum - j
            # 현재 보고있는 좌표: i 행 j 열

            if i < 0 or i >= N: continue  # 격자를 벗어나는 위치는 무시하기
            if a[i][j] == 0: continue  # 부서진 포탑이면 무시하기

            if minV > a[i][j]:
                minV, maxT, minI, minJ = a[i][j], lastAttack[i][j], i, j
            elif minV == a[i][j] and maxT < lastAttack[i][j]:
                minV, maxT, minI, minJ = a[i][j], lastAttack[i][j], i, j

    return minI, minJ


def select_target() -> tuple:  # 공격 대상을 선정하는 함수, O(NM)
    maxV, minT, maxI, maxJ = -1, INF, 0, 0
    for sum in range(N + M - 1):
        for j in range(M):
            i = sum - j

            if i < 0 or i >= N: continue
            if maxV < a[i][j]:
                maxV, minT, maxI, maxJ = a[i][j], lastAttack[i][j], i, j
            elif maxV == a[i][j] and minT > lastAttack[i][j]:
                maxV, minT, maxI, maxJ = a[i][j], lastAttack[i][j], i, j

    return maxI, maxJ


def tryRaser(atk, tgt) -> bool:  # 레이저 공격 시도, 실패하면 False return, O(NM)
    # visit[x][y] := x행 y열에 대한 방문 여부
    visit = [[False for _ in range(M)] for _ in range(N)]

    # come[x][y] := x행 y열이 어디로부터 왔는가?
    come = [[None for _ in range(M)] for _ in range(N)]

    # 우/하/좌/상 우선순위로 네 방향을 본다.
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    q = deque()
    q.append(atk)
    visit[atk[0]][atk[1]] = True

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = (x + dx + N) % N, (y + dy + M) % M
            if visit[nx][ny]: continue
            if a[nx][ny] == 0: continue
            come[nx][ny] = (x, y)  # 어디로부터 왔는지 기록하기
            visit[nx][ny] = True
            q.append((nx, ny))

    if not visit[tgt[0]][tgt[1]]:  # 만약 레이저가 도달하지 못했다면, False return
        return False

    x, y = tgt
    while x != atk[0] or y != atk[1]:
        # power 공격력 정하기
        power = a[atk[0]][atk[1]] // 2
        if x == tgt[0] and y == tgt[1]:
            power = a[atk[0]][atk[1]]

        # 공격하기
        attack(x, y, power)

        # 역추적하기
        x, y = come[x][y]

    return True


def bomb(atk, tgt):  # 포탄 공격하기 O(1)
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            nx, ny = (tgt[0] + dx + N) % N, (tgt[1] + dy + M) % M
            if nx == atk[0] and ny == atk[1]: continue

            # 공격력 정하기
            power = a[atk[0]][atk[1]] // 2
            if nx == tgt[0] and ny == tgt[1]: power = a[atk[0]][atk[1]]

            # 공격하기
            attack(nx, ny, power)


for tm in range(1, K + 1):
    if isFinish():  # 만약 종료 조건을 만족했다면, 턴을 수행하지 않고 종료
        break

    # 1. 공격자 선정
    atk = select_attacker()

    # 2. 공격 대상 선정
    tgt = select_target()

    # 3. 공격자에게 핸디캡 적용
    a[atk[0]][atk[1]] += N + M

    # 4. 공격자에 대해 "마지막 공격 턴" 정보 갱신
    lastAttack[atk[0]][atk[1]] = tm

    # 5. 공격 수행
    isAttacked = [[False for _ in range(M)] for _ in range(N)]
    isAttacked[atk[0]][atk[1]] = True
    if not tryRaser(atk, tgt):  # 레이저 공격을 시도하기
        bomb(atk, tgt)  # 실패했다면 포탄 공격

    # 6. 정비 수행
    for i in range(N):
        for j in range(M):
            if not isAttacked[i][j] and a[i][j] != 0:  # 공격에 가담하지 않은 포탑이라면
                a[i][j] += 1  # 공격력 1 증가

res = select_target()
print(a[res[0]][res[1]])

# => 전체 시간 복잡도: O(K * N * M)
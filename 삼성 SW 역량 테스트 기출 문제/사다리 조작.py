n, m, h = map(int, input().split())  # n: 세로선 개수 / m: 가로선 개수 / h: 세로선마다 가로선을 놓을 수 있는 위치의 개수
grid = [[0] * (h + 1) for _ in range(n + 1)]

for _ in range(m):
    # b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다
    a, b = map(int, input().split())  # 가로선 정보 (1 ≤ a ≤ H, 1 ≤ b ≤ N-1)
    grid[b][a] = b + 1
    grid[b + 1][a] = b


# 사다리 게임은 각각의 세로선마다 게임을 진행하고, 세로선의 가장 위에서부터 아래 방향으로 내려가야 한다.
# 이때, 가로선을 만나면 가로선을 이용해 옆 세로선으로 이동한 다음, 이동한 세로선에서 아래 방향으로 이동해야 한다.
def sadari():
    for c in range(1, n + 1):
        idx = c
        for r in range(1, h + 1):
            # 가로선이 있니?
            if grid[idx][r]:
                idx = grid[idx][r]
        if idx != c:
            return False
    return True


ans = 4


def dfs(cnt):
    global ans
    if sadari():
        ans = ans if ans < cnt else cnt
    elif cnt == 3 or ans <= cnt:
        return
    for c in range(1, n):
        flag = False    # 중복 조사를 하지 않기 위해 필요.
        # 아래를 보자. 아무 가로선이 없을 때, 2개의 가로선을 다음과 같이 추가해보자.

        # 1 2 3    1 2 3
        # | | |    |-| |
        # |-| | 와 | | |  는 같은 결과이다. 하지만 만약 가로 줄 사이(r~R)에 다른 가로선이 있거나,
        # |-| |    |-| |                 가로줄 사이(r~R)에 양 옆 세로에 가로선이 있다면
        #                                결과가 달라질 수 있기때문에 조사해줘야한다.

        for r in range(1, h + 1):
            if flag and grid[c][r] == 0 and grid[c + 1][r] == 0:    # 이미 위에서 가로선을 추가했고, 현재 가로선이 없다면 중복이기 때문에 조사 안해도 됨.
                continue
            else:
                flag = False
            if grid[c][r] == 0 and grid[c + 1][r] == 0:
                grid[c][r] = c + 1
                grid[c + 1][r] = c
                dfs(cnt + 1)
                grid[c][r] = 0
                grid[c + 1][r] = 0
                flag = True     # i번째 dfs에서 가로선(r)을 추가한 이후 i+1번째 dfs에서 다른 가로선을 모두 조사하고, i번째로 돌아와서 그었던 가로선을 지웠다.
                                # 그렇다면 flag=True로 두어서 그 이후에 다른 가로선이 나올 때 까지는 가로선을 추가 안해도 된다.
                                # 왜냐하면 다음 행(r+1~)에서 추가적인 가로선이 존재하지 않을 때, r번째 가로선이 존재할 때의 모든 상황을 조사하였으므로
                                # r+1번째 행에 가로선을 그어도 똑같은 결과가 나오기 때문.


dfs(0)
print(ans if ans < 4 else -1)

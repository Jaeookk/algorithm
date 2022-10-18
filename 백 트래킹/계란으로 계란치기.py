import sys

input = sys.stdin.readline
n = int(input().rstrip())
eggs = []
result = 0
for _ in range(n):
    eggs.append(list(map(int, input().rstrip().split())))


def dfs(depth):
    global result

    if depth == n:  # depth가 n이 되면 깨진 계란 갯수세고 리턴
        cnt = 0
        for i in eggs:
            if i[0] <= 0:
                cnt += 1
        if cnt > result:
            result = cnt
        return

    if eggs[depth][0] <= 0:  # 계란이 깨진계란일때 바로 다음 계란로 진행
        dfs(depth + 1)
    else:
        flag = False
        for i in range(n):
            # 계란을 부딪힐 수 있는 경우(자기자신 제외, 내구도 1이상)
            if i != depth and eggs[i][0] > 0:
                flag = True
                eggs[i][0] -= eggs[depth][1]
                eggs[depth][0] -= eggs[i][1]
                dfs(depth + 1)
                eggs[i][0] += eggs[depth][1]
                eggs[depth][0] += eggs[i][1]

        if not flag:  # 계란이 전부 깨져있을때 바로 depth = n으로 진행
            dfs(n)


dfs(0)
print(result)

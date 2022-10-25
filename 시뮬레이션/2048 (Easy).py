# 각 방향으로 기울여서 미는것은 그래프를 회전하고 한 방향으로 미는것으로 생각.
# 미는 것은 왼쪽으로 미는것으로 통일하고, 그래프를 회전시키고 밀면 상,하,좌,우로 미는 것을 표현할 수 있다.
def rotation(arr):
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[j][n - i - 1] = arr[i][j]
    return temp


def dfs(depth, graph):
    global result

    if depth == 5:  # 5번 이동했다면 그때의 최대값을 비교.
        for i in range(n):
            x = max(graph[i])
            if result < x:
                result = x
        return

    for _ in range(4):  # 총 4번 회전해야하니까
        array = rotation(graph)  # 회전
        temp = [[0 for _ in range(n)] for _ in range(n)]  # 임시 보드

        for i in range(n):  # 각 행을 기준으로
            idx = 0
            for j in range(n):
                if array[i][j] == 0:  # 만약 게임보드의 값이 0이면 다음 column 조사
                    continue

                if temp[i][idx] == 0:  # 임시 보드의 idx번째 값이 0이면
                    temp[i][idx] = array[i][j]  # 임시 보드의 idx번째 값을 채움

                elif temp[i][idx] == array[i][j]:  # 임시 보드의 idx 값과 보드의 값이 같으면
                    temp[i][idx] = temp[i][idx] * 2  # 합치기
                    idx += 1  # 임시 보드의 칸은 오른쪽으로 한 칸 이동

                elif temp[i][idx] != array[i][j]:  # 임시 보드의 값과 보드의 값이 다르면
                    idx += 1  # 임시 보드의 칸은 오른쪽으로 한 칸 이동
                    temp[i][idx] = array[i][j]  # 이동한 임시 보드의 칸에 값을 추가.

        graph = temp  # 게임 보드를 한 번 회전한 것에 대하여 왼쪽으로 쭉 밀었을때의 결과로 바꾸기
        dfs(depth + 1, graph)  # 다음 이동 조사
        graph = array  # 게임 보드를 다시 되돌리기


if __name__ == "__main__":
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    dfs(0, graph)
    print(result)

# 임시보드와 게임보드의 관계를 그림으로 설명하자면(line25~40)

# 게임: 0 2 0 2 8 8 0 16
# 임시: 0 0 0 0 0 0 0 0

#         v
# 게임: 0 2 0 2 8 8 0 16
# 임시: 2 0 0 0 0 0 0 0

#             v
# 게임: 0 2 0 2 8 8 0 16
# 임시: 4 0 0 0 0 0 0 0

#               v
# 게임: 0 2 0 2 8 8 0 16
# 임시: 4 8 0 0 0 0 0 0

#                 v
# 게임: 0 2 0 2 8 8 0 16
# 임시: 4 16 0 0 0 0 0 0

#                       v
# 게임: 0 2  0  2 8 8 0 16
# 임시: 4 16 16 0 0 0 0 0  << 이때 16과 16이 안합쳐지는 이유는 처음 16은 이미 8과8이 합쳐졌기 때문
# 문제에서 "한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다." 라고 설명함.

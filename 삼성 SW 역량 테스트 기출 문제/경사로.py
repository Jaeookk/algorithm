def check_line(arr):
    """
    층이 바꼈을 때, 그 크기가 1이라면.
    1. 높은 층 -> 낮은 층 : 경사로가 들어갈 크기가 되는지
    2. 낮은 층 -> 높은 층 : 경사로가 이미 있는지, 있으면 추가 경사로가 겹치지 않고 들어가는지
    """
    slope = [False]*N

    for i in range(N-1):
        if abs(arr[i] - arr[i+1]) > 1:
            return False

        if arr[i] > arr[i+1]:   # 높 -> 낮
            for j in range(L):  # 경사로가 놓일 모든 범위에 대하여 조사
                if i + 1 + j >= N or arr[i+1] != arr[i+1+j] or slope[i+1+j]:
                    # 경사로가 범위를 초과하거나
                    # 경사로가 같은 높이에 위치해있지 못하거나
                    # 이미 해당 위치에 경사로가 있다면(겹친다면)
                    return False
                if arr[i+1] == arr[i+1+j]:
                    # 경사로 추가
                    slope[i+1+j] = True

        elif arr[i] < arr[i+1]:     # 낮 -> 높
            for j in range(L):
                if i-j < 0 or arr[i] != arr[i-j] or slope[i-j]:
                    return False
                if arr[i] == arr[i-j]:
                    slope[i-j] = True
    return True


if __name__ == "__main__":
    N, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        if check_line([graph[i][j] for j in range(N)]):
            result += 1
        if check_line([graph[j][i] for j in range(N)]):
            result += 1

    print(result)

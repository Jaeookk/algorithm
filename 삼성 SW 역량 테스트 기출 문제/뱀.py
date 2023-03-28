def solution(x, y, L):
    # (x,y) -> 뱀의 머리 위치
    Map[x][y] = 2  # 뱀이 있으면 : 2
    rotate_info = 0
    body = [(0, 0)]  # 뱀의 전체 위치
    time = 0
    indices = 0

    while True:
        if indices < L and time == int(info[indices][0]):
            # 방향 구하기, 현재 방향을 [동, 남, 서, 북]으로 정의
            #  왼쪽 회전시  -> -1 후 % 4
            # 오른쪽 회전시 -> +1 후 % 4
            # 4로 나눈 나머지를 구하는 이유는 rotate_info가 0미만 or 4이상이 되었을때 0 ~ 3 사이의 값을 구해주기 위함
            # ex) 동쪽 일때 왼쪽 회전 -> rotate_info가 0에서 -1 -> 4로 나눈 나머지는 3 -> 3번째 인덱스 값은 북쪽
            # ex) 북쪽 일때 오른쪽 회전 -> roatate_info 3에서 4 -> 4로 나눈 나머지는 0 -> 0번째 인덱스 값은 동쪽
            if info[indices][1] == "L":
                rotate_info -= 1  # -1% 4 -> 3
                rotate_info %= 4
            elif info[indices][1] == "D":
                rotate_info += 1
                rotate_info %= 4
            indices += 1

        time += 1
        nx = x + dx[rotate_info]
        ny = y + dy[rotate_info]

        if nx >= 0 and nx <= n - 1 and ny >= 0 and ny <= n - 1:
            # 사과가 있을 경우
            if Map[nx][ny] == 1:
                Map[nx][ny] = 2
                body.append((nx, ny))
                x, y = nx, ny  # 뱀 머리 위치 갱신

            # 사과가 없을 경우
            elif Map[nx][ny] == 0:
                Map[nx][ny] = 2
                body.append((nx, ny))
                a, b = body.pop(0)  # 꼬리 이동
                Map[a][b] = 0  # 꼬리 비우기
                x, y = nx, ny  # 뱀 머리 위치 갱신

            # 꼬리와 부딪힌 경우
            elif Map[nx][ny] == 2:
                return time

        else:
            return time


if __name__ == "__main__":
    n = int(input())
    k = int(input())

    # 보드
    Map = [[0] * n for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        Map[a - 1][b - 1] = 1  # 사과 : 1, 빈칸 : 0

    # 방향전환
    info = []
    L = int(input())
    for _ in range(L):
        a, b = input().split()
        info.append((a, b))

    # 동,남,서,북
    dx = [0, 1, 0, -1]  # 행
    dy = [1, 0, -1, 0]  # 열

    print(solution(0, 0, L))

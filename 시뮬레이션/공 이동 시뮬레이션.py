# https://school.programmers.co.kr/learn/courses/30/lessons/87391?language=python3#
# 쿼리를 역순으로 돌아서 정답 칸에서 시작해서 쿼리를 돌면서 가능한 시작점의 범위를 구하기

def solution(n, m, x, y, queries):
    answer = 0
    x_min, x_max, y_min, y_max = x, x, y, y

    for dir, dist in queries[::-1]:
        if dir == 0:  # 좌(오른쪽에서 왔음)
            y_max += dist  # 오른쪽으로 늘리기
            if y_max > m - 1: # 범위 벗어나면
                y_max = m - 1  # 끝값으로
            if y_min != 0:  # 왼쪽 값이 끝이 아니면 범위 축소
                y_min += dist

        elif dir == 1:  # 우(왼쪽에서 왔음)
            y_min -= dist
            if y_min < 0:
                y_min = 0
            if y_max != m - 1:
                y_max -= dist

        elif dir == 2:  # 상(아래서 왔음)
            x_max += dist
            if x_max > n - 1:
                x_max = n - 1
            if x_min != 0:
                x_min += dist

        else:  # 하(위에서 왔음)
            x_min -= dist
            if x_min < 0:
                x_min = 0
            if x_max != n - 1:
                x_max -= dist
        if y_min > m - 1 or y_max < 0 or x_min > n - 1 or x_max < 0:
            # 반례 n = 1000,m = 1000 x=1,y=1 query = [[0,100001],[2,100001]] 처럼
            # 중간에 범위를 아예 벗어나서 결과가 0인 경우가 발생
            return answer
    else:
         answer = (y_max - y_min + 1) * (x_max - x_min + 1)
    return answer
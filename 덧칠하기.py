# https://school.programmers.co.kr/learn/courses/30/lessons/161989?language=python3
def solution(n, m, section):
    answer = 0
    painted_wall = section[0] - 1  # 페인트 칠할 곳 바로 이전 벽

    for x in section:
        if painted_wall < x:  # 페인트칠해진곳이 페인트 칠할 곳 보다 이전에 있다면
            # 페인트 최신화
            painted_wall = x + m - 1
            answer += 1

    return answer

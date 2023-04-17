# https://school.programmers.co.kr/learn/courses/30/lessons/181187

from math import ceil, sqrt


def solution(r1, r2):
    answer = 0
    for x in range(1, r2 + 1):
        max_y = int(sqrt(r2**2 - x**2))
        min_y = 0 if x > r1 else ceil(sqrt(r1**2 - x**2))
        answer += max_y - min_y + 1

    return answer * 4

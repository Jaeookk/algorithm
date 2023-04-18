# https://school.programmers.co.kr/learn/courses/30/lessons/181188#
# 프로그래머스 단속카메라와 같은 문제.


def solution(targets):
    answer = 1
    targets.sort(key=lambda x: x[1])

    start, end = targets[0]
    for i in range(1, len(targets)):
        if end <= targets[i][0]:
            answer += 1
            start, end = targets[i]

    return answer

# 프로그래머스 레벨3
# 누적합
# https://school.programmers.co.kr/learn/courses/30/lessons/161988


def solution(sequence):
    n = len(sequence)
    psum = [0] * (n + 1)

    for i in range(n):
        psum[i + 1] = psum[i] + sequence[i] * (-1) ** i

    return max(psum) - min(psum)

# https://school.programmers.co.kr/learn/courses/30/lessons/12979

import math


def solution(n, stations, w):
    answer = 0
    electric_wave = 1 + 2 * w
    start = 0

    for station in stations:
        distance = station - w - start - 1  # 기지국 기준 왼쪽에 전파가 도달하지 않는 거리 구하기
        answer += math.ceil(distance / electric_wave)  # 기지국 개수 더해주기
        start = station + w  # 해당 기지국의 전파가 끝나는 지점(오른쪽)

    if start < n:  # 마지막 기지국의 오른쪽 전파가 마지막 아파트까지 도달하지 않았다면
        distance = n - start  # 아파트 개수 구하기
        answer += math.ceil(distance / electric_wave)  # 기지국 설치

    return answer

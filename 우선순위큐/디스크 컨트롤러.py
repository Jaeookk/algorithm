# Programmers Lv.3
# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq


def solution(jobs):
    answer = 0
    heap = []

    start, now, global_time = -1, 0, 0

    while global_time < len(jobs):
        for i in jobs:
            # 현재 시점에서 처리할 수 있는 작업들을 힙에 넣기
            # 작업의 요청 시간이 바로 이전에 완료한 작업의 시작 시간(start)보다 크고 현재 시점(now)보다 작거나 같아야 한다.
            if start < i[0] <= now:
                heapq.heappush(heap, [i[1], i[0]])  # 작업의 소요 시간 기준으로 최소힙 만들기

        if len(heap) > 0:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1]
            global_time += 1
        else:  # 만약 현재 처리할 수 있는 작업이 없다면,
            now += 1  # 남아 있는 작업들의 요청 시간이 아직 오지 않은 것이기 때문에 현재 시점(now)을 하나 올려준다.

    return int(answer / len(jobs))

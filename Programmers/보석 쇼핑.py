# 프로그래머스 LV.3
# 2020 카카오 인턴십
# 투 포인터

from collections import Counter, defaultdict


def solution(gems):
    answer = []
    count = Counter(gems)
    total = len(count)

    end = 0
    res = defaultdict(int)
    cnt = 100000
    for start in range(len(gems)):
        while len(res) < total and end < len(gems):
            # res.append(gems[end])
            res[gems[end]] += 1
            end += 1

        if len(res) == total and cnt > end - start:
            answer = [start + 1, end]
            cnt = end - start

        res[gems[start]] -= 1
        if res[gems[start]] == 0:
            del res[gems[start]]

    return answer

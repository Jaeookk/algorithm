from itertools import permutations


def solution(k, dungeons):
    answer = -1
    datas = list(permutations(dungeons, len(dungeons)))
    for data in datas:
        tmp = k
        count = 0
        for min, consume in data:
            if tmp >= min:
                tmp -= consume
                count += 1
        answer = max(answer, count)

    return answer

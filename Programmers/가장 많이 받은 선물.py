def solution(friends, gifts):
    # https://school.programmers.co.kr/learn/courses/30/lessons/258712

    l = len(friends)
    res = [0] * l
    f_idx = {friend: i for i, friend in enumerate(friends)}
    give_n_take = [[0 for _ in range(l)] for _ in range(l)]
    record = [[0, 0, 0] for _ in range(l)]

    for gift in gifts:
        giver, reciever = gift.split(" ")
        give_n_take[f_idx[giver]][f_idx[reciever]] += 1
        record[f_idx[giver]][0] += 1
        record[f_idx[reciever]][1] += 1

    for i in range(l):
        record[i][-1] = record[i][0] - record[i][1]

    for j in range(l):
        for k in range(l):
            if give_n_take[j][k] != 0 and give_n_take[j][k] > give_n_take[k][j]:  # j가 k에게 선물 더 많이 줬다면
                res[j] += 1
            elif give_n_take[j][k] == give_n_take[k][j] and record[j][-1] > record[k][-1]:
                # j와 k가 주고받은 선물이 하나도 없거나, 주고받은 수가 같다면 선물 지수가 더 큰 사람이 선물을 받기.
                res[j] += 1

    return max(res)

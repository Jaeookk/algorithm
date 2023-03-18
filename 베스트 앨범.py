# https://school.programmers.co.kr/learn/courses/30/lessons/42579


def solution(genres, plays):
    answer = []
    dic = dict()
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre in dic.keys():
            dic[genre] = [dic[genre][0] + play, dic[genre][1] + [(play, i)]]
        else:
            dic[genre] = [play, [(play, i)]]

    for _, value in sorted(dic.items(), key=lambda x: -x[1][0]):
        # dic.items() -> (key, value) 니까 -x[1][0] -> value[0] (play의 합)에 따라 내림차순
        cnt = 0
        for j in sorted(value[1], key=lambda x: (-x[0], x[1])):
            # 장르 내에서 많이 재생된 노래 & 고유 번호가 낮은 순으로 정렬
            if cnt < 2:
                answer.append(j[1])
                cnt += 1

    return answer

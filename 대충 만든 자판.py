# https://school.programmers.co.kr/learn/courses/30/lessons/160586?language=python3
def solution(keymap, targets):
    answer = []
    #최솟값 저장
    alpha = [101 for i in range(26)]
    for i in keymap:
        for idx, j in enumerate(i):
            k = ord(j) - ord('A')
            alpha[k] = min(alpha[k], idx + 1)

    for i in targets:
        total = 0
        for j in i:
            cnt = alpha[ord(j) - ord('A')]
            if cnt == 101:
                answer.append(-1)
                break
            else:
                total += cnt
        else:
            answer.append(total)

    return answer

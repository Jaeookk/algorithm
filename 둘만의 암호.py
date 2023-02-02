# https://school.programmers.co.kr/learn/courses/30/lessons/155652
def solution(s, skip, index):
    answer = ''
    for i in range(len(s)):
        askii = ord(s[i])
        count = 0
        while True:
            askii += 1
            if askii > 122:
                askii = 97
            if chr(askii) not in skip:
                count += 1
            if count == index:
                answer += chr(askii)
                break
    return answer

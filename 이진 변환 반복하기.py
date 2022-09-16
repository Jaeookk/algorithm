# https://school.programmers.co.kr/learn/courses/30/lessons/70129
def solution(s):
    zero_count = 0
    cnt = 0
    while True:
        if s == "1":
            break
        zero_count += s.count("0")
        cnt += 1
        s = s.replace("0", "")
        tmp = len(s)
        result = []
        while tmp > 0:
            k = tmp % 2
            tmp = tmp // 2
            result.append(str(k))
        result.reverse()
        s = "".join(result)
        # print(s)
    answer = [cnt, zero_count]
    return answer

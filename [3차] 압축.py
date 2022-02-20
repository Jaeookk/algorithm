def solution(msg):
    answer = []
    alpha, i, s = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], 0, msg[0]

    while i != len(msg):
        if s in alpha:
            if i != len(msg)-1:
                i += 1
            else: # i 가 msg의 마지막 인덱스 일때
                answer.append(alpha.index(s)+1)
                break
            s += msg[i]
        else:
            alpha.append(s)
            answer.append(alpha.index(s[:-1])+1)
            s = msg[i]

    return answer

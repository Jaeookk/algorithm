# https://school.programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    answer = []
    new_s = s[2:-2].split('},{')
    new_s = sorted(new_s, key=lambda x: len(x))

    # memory = set()
    # for char in new_s:
    #     tmp = set(list(map(int, char.split(','))))
    #     answer += list(tmp.difference(memory))
    #     memory = tmp
    
    for i in new_s:
        i = list(map(int, i.split(',')))
        for j in i:
            if j not in answer:
                answer.append(j)
    
    return answer

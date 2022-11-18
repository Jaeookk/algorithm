# https://school.programmers.co.kr/learn/courses/30/lessons/134240
def solution(food):
    answer = ''
    temp = ''
    for i in range(1,len(food)):
        if food[i] > 1:
            temp += str(i)*(food[i]//2)
    # print(''.join(reversed(temp)))
    answer += temp + '0' + temp[::-1]

    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/150370
def change_to_day(date):
    y, m, d = map(int, date.split("."))
    return y*28*12 + m*28 + d

def solution(today, terms, privacies):
    answer = []
    today = change_to_day(today)
    
    dic = {x[0]:int(x[2:])*28 for x in terms}

    answer = [idx+1 for idx, privacy in enumerate(privacies) if change_to_day(privacy[:-2]) + dic[privacy[-1]] <= today]
        
        
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    answer = []
    id_name = dict()
    checking = []
    
    for info in record:
        check, *last = info.split(" ")
        if len(last) ==2:
            id_name[last[0]] = last[1]
        if check == "Enter" or check == "Leave":
            checking.append((check,last[0]))
    
    for x,id in checking:
        if x == "Enter":
            answer.append(id_name[id]+"님이 들어왔습니다.")
        else:
            answer.append(id_name[id]+"님이 나갔습니다.")
    
    return answer

def solution(id_list, report, k):
    answer = [0]*len(id_list)
    user = {x:[] for x in id_list}
    reported = {x:0 for x in id_list}
    
    for i in set(report):
        name = i.split()[0]
        re_name = i.split()[1]
        user[name].append(re_name)
        reported[re_name] += 1
        
    idx = 0
    for value in user.values():
        for i in value:
            if reported[i] >= k:
                answer[idx] += 1
        idx += 1
    
    return answer

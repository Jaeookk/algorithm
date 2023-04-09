def solution(plans):
    answer = []
    for idx in range(len(plans)):
        hour, min = map(int, plans[idx][1].split(":"))
        start = hour * 60 + min
        end = start + int(plans[idx][2])
        plans[idx][1], plans[idx][2] = start, end

    plans.sort(key=lambda x: (x[1], x[2]))
    stop_subject = []

    subject, start, end = plans[0]

    for i in range(1, len(plans)):
        if plans[i][1] < end:
            # 지금 과제가 끝나기 전에 다음 과제를 시작해야 된다면
            stop_subject.append([subject, end - plans[i][1]])  # 리스트에 지금 과제 저장
            subject, start, end = plans[i]  # 과제 최신화

        elif plans[i][1] > end:  # 다음 과제가 시작하기 전에 지금 과제가 끝난다면
            answer.append(subject)  # 지금 과제를 끝내고
            empty_time = plans[i][1] - end  # 공강시간 계산

            while stop_subject and empty_time > 0:  # 공강시간만큼 중단했던 과제들 처리
                if empty_time >= stop_subject[-1][1]:
                    a, b = stop_subject.pop()
                    answer.append(a)
                    empty_time -= b
                else:
                    stop_subject[-1][1] -= empty_time
                    break
            subject, start, end = plans[i]  # 다음 과제로 최신화

        else:  # plans[i][1] == end
            answer.append(subject)
            subject, start, end = plans[i]

    answer.append(subject)
    for i in range(len(stop_subject) - 1, -1, -1):
        answer.append(stop_subject[i][0])

    return answer


# def solution(plans):
#     plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])
#     # 시작 시간 기준 내림차순

#     lst = [] # 과제들이 각각 끝나는 시간을 담을 리스트
#     while plans:
#         x = plans.pop() # 가장 빠른 시작시간의 과제
#         for i, v in enumerate(lst):
#             if v[0] > x[1]: # 만약 먼저 시작했던 과제의 끝나는 시간이, 지금 과제의 시작시간보다 크다면
#                 lst[i][0] += x[2] # 지금 과제가 끝날 때 까지 걸리는 시간만큼 더 늦게 끝나니까
#         lst.append([x[1] + x[2], x[0]]) # 이후 리스트에 현재 과제의 종료시간 추가
#     lst.sort() # 오름차순 정렬

#     return list(map(lambda x: x[1], lst)) # 과제 이름만 출력

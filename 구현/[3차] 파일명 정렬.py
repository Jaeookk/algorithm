# https://school.programmers.co.kr/learn/courses/30/lessons/17686#
def solution(files):
    answer = []
    temp = []
    for idx, file in enumerate(files):
        for i in range(len(file)):
            if file[i].isdecimal():
                start = i # 숫자가 처음 나오는 지점
                break
                
        end = start + 5 # 숫자는 0~99999 사이이므로 최대 5개
        cnt = 0
        for j in file[start:end]:
            if not j.isdecimal():
                end = start + cnt  # 숫자가 끝나는 지점, 즉 tail의 시작 지점을 구해주고
                break
            cnt += 1

                
        head, num, tail = file[:start], file[start:end], file[end:]
        temp.append((head.lower(),num.zfill(5),tail, idx)) # head는 소문자로 통일, 숫자는 5자리 맞추기
        
    temp = sorted(temp, key=lambda x: (x[0],x[1]))
    
    for *x,i in temp:
        answer.append(files[i])
        
    return answer

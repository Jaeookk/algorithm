# https://school.programmers.co.kr/learn/courses/30/lessons/17683
def convert(x):
    x += ' ' # 치환을 위해 2개씩 조사할거기 때문에 빈칸 추가
    result = ''
    for i in range(len(x)-1):
        if x[i+1] == "#":
            result += x[i].lower()  # ex) C#인 경우 소문자 c로 치환
        elif x[i] == "#":
            continue
        else:
            result += x[i]
    return result


def solution(m, musicinfos):
    neo = convert(m)
            
    info = []
    for x in musicinfos:
        temp = ''
        *time, title, melody = x.split(",")
        time = (int(time[1][0:2]) * 60 + int(time[1][-2:])) - (int(time[0][0:2]) * 60 + int(time[0][-2:]))
        temp = convert(melody)
        info.extend([(time, title, temp)]) # 해석하기 쉽게 변환한 정보들을 info에 추가
    
    result = []
    for i, (time, title, melody) in enumerate(info):
        if time <= len(melody): # 재생시간보다 노래의melody가 크거나 같은 경우
            if neo in melody[:time]: # 만약 네오가 들은 멜로디가 재생시간동안 재생된 멜로디에 포함된경우
                result.append((i, time, title)) # 순서, 재생시간, 제목
        
        else: # 노래의melody보다 재생시간이 긴 경우 -> 노래의melody 반복 재생
            x,y = time // len(melody), time % len(melody)
            tmp = melody * x + melody[:y]
            if neo in tmp :
                result.append((i, time, title))
                
    if result:
        result = sorted(result, key=lambda x: (-x[1], x[0]))
        return result[0][-1]
    else:
        return "(None)"

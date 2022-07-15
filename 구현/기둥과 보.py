def check(answer):
    for x, y, structure in answer:
        if structure == 0: # 기둥인 경우
            # answer에 있는 구조들이 조건에 부합한지 확인
            if y == 0 or [x,y,1] in answer or [x-1, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False
        if structure == 1: # 보인 경우
            # answer에 있는 구조들이 조건에 부합한지 확인
            if [x,y-1,0] in answer or [x+1, y-1, 0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, structure, way in build_frame:
        if way == 0: # 삭제
            answer.remove([x, y, structure])
            if check(answer) == 0:
                answer.append([x, y, structure])
        if way == 1: # 설치
            answer.append([x, y, structure])
            if check(answer) == 0:
                answer.remove([x, y, structure])
    answer.sort()
    
    return answer

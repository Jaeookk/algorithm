# https://school.programmers.co.kr/learn/courses/30/lessons/131130
def solution(cards):
    answer = []
    boxes = {idx+1: card for idx, card in enumerate(cards)}
    # print(boxes)
    while boxes:
        visited = set()
        pos = list(boxes.keys())[0]
        while pos not in visited:
            visited.add(pos)
            tmp = boxes[pos]
            del boxes[pos]
            pos = tmp
        answer.append(len(visited))
    answer.sort(reverse=True)
    
    if len(answer) > 1:
        return answer[0]*answer[1]
    else:
        return 0

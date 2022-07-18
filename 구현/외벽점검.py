from itertools import permutations

def solution(n, weak, dist):
    result = []
    length = len(weak)
    for i in range(len(weak)):
        weak.append(weak[i] + n)
    print(weak)
    all_dist = list(permutations(dist, len(dist)))
    
    
    for w in range(length):
        for d in all_dist:
            cnt = 1 # 친구 수
            distance = weak[w] + d[cnt - 1]
            for i in range(w, w + length): # 취약 지점 시작점부터 끝 취약지점 까지
                if distance < weak[i]: # 친구가 다음 취약지점에 도달하지 못했다면
                    cnt += 1 # 친구 1명 추가
                    if cnt > len(dist): # 친구들을 모두 투입해도 취약 지점을 전부 점검할 수 없는 경우. 다음 순열을 조사
                        break
                    distance = weak[i] + d[cnt - 1]
            result.append(cnt)
    answer = min(result)
    if answer > len(dist):
        return -1
    else:
        return answer

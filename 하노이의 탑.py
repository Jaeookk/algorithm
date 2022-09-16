# https://school.programmers.co.kr/learn/courses/30/lessons/12946
def move(start, end, mid, n, answer):
    if n == 1:
        # 시작지 -> 목적지를 answer에 리스트로 저장한다
        answer.append([start, end])
        return
    # 1. 위에서부터 n-1개의 원반을 a에서 c를 거쳐 b로 이동시킨다. 그래야 맨 마지막 원반을 원하는 목적지로 이동시킬 수 있다.
    move(start, mid, end, n - 1, answer)
    # 2. 맨 아래에 있던 갖아 큰 원반을 a에서 c로 이동시킨다.
    answer.append([start, end])
    # 3. b로 이동시켰던 n-1개의 원반을 b에서 a를 거쳐 c로 이동시킨다.
    move(mid, end, start, n - 1, answer)


def solution(n):
    answer = []
    move(1, 3, 2, n, answer)
    x = []
    move(1, 3, 2, 4, x)
    print(x)
    return answer

# BOJ 11286
# 1. 배열에 정수 x (x ≠ 0)를 넣는다.
# 2. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
#     절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        # 절대값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력해야 한다.
        # 어떻게 가능할까?
        # heapq 모듈은 원소들이 무슨 타입이든 내부적으로 < 비교 연산자를 사용하고,
        # int, string, tuple, list 등 자주 쓰이는 타입들에 대하여 < 연산자의 의미가 각각 정의되어 있기 때문에 그 정의대로 동작한다.
        # 파이썬에서 튜플 2개를 비교할 때는 왼쪽부터 같은 위치의 원소끼리 서로 비교하다가 먼저 끝나거나 더 작은 원소가 나오는 쪽이 작다.
        # 따라서 abs(x)가 같은 튜플 중에는 x가 작은 것이 먼저 뽑힌다.
        heapq.heappush(heap, (abs(x), x))

    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)

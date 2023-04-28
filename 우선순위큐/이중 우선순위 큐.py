# BOJ 7762 골드4
import sys
import heapq
from collections import defaultdict


def sync(heap, x=1):
    while heap and not exist[heap[0] * x]:  # 힙이 비어있지 않고, heap[0]이 존재하지 않다면 삭제
        heapq.heappop(heap)


input = sys.stdin.readline
T = int(input())
for test_case in range(T):
    max_heap = []
    min_heap = []
    k = int(input())
    exist = defaultdict(int)

    for i in range(k):
        s, num = input().split()

        if s == "I":
            n = int(num)
            if not exist[n]:  # n이 없다면 힙에 추가 (힙에 중복 추가 방지 -> 삭제 시 반복 안해도 됨.)
                heapq.heappush(max_heap, -n)
                heapq.heappush(min_heap, n)
            exist[n] += 1  # 얘는 왜 밖에 꺼내져 있느냐.
            # 만약 같은 원소가 입력되면 힙에는 한 번만 추가하지만, 카운트는 계속 해줘야함
            # 왜냐하면 예를들어 I 5, I 5, I 5, D 1 이렇게 입력이 들어왔다.
            # if문 안에 있었다면 heap = [5], exist = {5 : 1} 일 것이고, D 1 때문에 삭제후 heap과 exist는 빈 자료구조가 되어 버린다.
            # 하지만 if문 밖으로 빼낸다면, heap = [5], exist = {5 : 3} 일 것이고, D 1 이후 heap = [5], exist = {5 : 2} 가 된다.

        else:
            if num == "1":
                sync(max_heap, -1)
                if not max_heap:
                    continue
                exist[-max_heap[0]] -= 1
                if not exist[-max_heap[0]]:
                    heapq.heappop(max_heap)

            elif num == "-1":
                sync(min_heap)
                if not min_heap:
                    continue
                exist[min_heap[0]] -= 1
                if not exist[min_heap[0]]:
                    heapq.heappop(min_heap)

    sync(max_heap, -1)
    sync(min_heap)

    if min_heap and max_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")

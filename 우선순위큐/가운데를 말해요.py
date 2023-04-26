# BOJ 1655 골드2

import sys
import heapq

input = sys.stdin.readline


left_heap, right_heap = [], []

for _ in range(int(input())):
    num = int(input())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)

    if left_heap and right_heap and left_heap[0] * -1 > right_heap[0]:
        max_value = heapq.heappop(left_heap) * -1
        min_value = heapq.heappop(right_heap)

        heapq.heappush(left_heap, min_value * -1)
        heapq.heappush(right_heap, max_value)

    print(left_heap[0] * -1)

# 1 -> 1
# 1 5 -> 1
# 1 2 5 -> 2
# 1 2 5 10 -> 2
# -99 1 2 5 10 -> 2
# -99 1 2 5 7 10 -> 2
# -99 1 2 5 5 7 10 -> 5

#      max   min
# 1 -> [-1], []
# 1 5 -> [-1] [5]
# 1 2 5 -> [-2, -1] [5]
# 1 2 5 10 -> [-2,-1] [5,10]
# -99 1 2 5 10 -> [-2, -1, 99] [5, 10]
# -99 1 2 5 7 10 -> [-2,-1,99] [5,10,7]
# -99 1 2 5 5 7 10 -> [-5,-2,-1,99] [5,7,10]

# 힙을 두 개 사용하자
# 왼쪽 힙은 최대 힙으로 정렬하고, 오른쪽 힙은 최소 힙으로 정렬하자.
# 두 개의 힙의 길이를 같게 유지하기 위해 번갈아가며 원소를 넣자.
# 이때 크기만 잘 구분해서 넣어준다면 왼쪽 힙의 첫번째 요소가 문제에서 요구한 중앙값이 된다.
#   왜? 왼쪽힙과 오른쪽 힙의 길이는 같고, 왼쪽힙의 첫 번째 요소는 최대힙에서 가장 큰 값이기 때문.
# 그렇다면 크기를 어떻게 구분해야 할까?
# 간단하다. 원소를 번갈아가면서 넣을 때 마다, 왼쪽힙의 가장 큰 값과 오른쪽 힙의 가장 작은 값을 대소비교해준다.
# 즉, 왼쪽 힙의 첫 번째 요소(가장 큰 값)이 오른쪽 첫번째 원소(가장 작은 값)보다 크다면 서로 값을 바꿔주면 된다.
# 이때 당연히 왼쪽 힙의 원소값에는 -1을 곱해줘야겠지?

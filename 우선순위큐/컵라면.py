# BOJ 1781 골드2
import sys
import heapq

input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    deadline, cup = map(int, input().split())
    heapq.heappush(heap, (deadline, -cup))

answer = 0
time = 1  # 현 시간
temp_heap = []
while heap:
    deadline, cup = heapq.heappop(heap)
    answer -= cup  # 우선 데드라인 안쪽이니 더해줌
    heapq.heappush(temp_heap, -cup)  # 더한 값들을 다 저장해줌

    while heap and time == heap[0][0]:  # 현재 시간과 같은 데드라인을 가지고 있는 문제들을 발견하면 다 빼내야함
        possible = heapq.heappop(heap)  # 여기서 데드라인이 긴 경우가 더 많은 라면을 얻을 수 있는 경우를 찾아냄
        if -possible[1] > temp_heap[0]:  # 데드라인이 긴 경우가 라면 획득량 > 획득했던 라면량중에 가장 적은 획득량
            answer -= heapq.heappop(temp_heap)  # 가장 적은 획득량을 빼고
            answer -= possible[1]  # 지금 라면 획득량을 더해줌
            heapq.heappush(temp_heap, -possible[1])  # 이건 다시 이때까지 획득했던 라면량으로 넣어줌
    time += 1  # 시간 +1

if answer > 2**31:
    print(2**31)
else:
    print(answer)

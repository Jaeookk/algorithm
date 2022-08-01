# 거리를 최대로 하는 최적화 문제.
# 거리로 이진탐색을 해보자.

import sys
f = sys.stdin.readline

# 집의 개수, 공유기의 개수
n, c = map(int, f().split())

array = []
for i in range(n):
    array.append(int(f()))

array.sort()

start = 1 # 최소 거리
end = array[-1] - array[0] # 최대 거리
result = 0

while(start <= end):
    mid = (start + end) // 2 # 공유기를 설치한 집 사이의 기준 거리

    a = array[0] # 첫 번째 집에 공유기 설치
    cnt = 1
    for i in range(1, n):
        # 모든 집을 순회하면서 설치해볼때 각 집의 거리가 기준보다 크다면 설치.
        if (array[i] - a) >= mid:
            a = array[i]
            cnt += 1

    # 만약 설치된 공유기가 조건보다 크거나 같다면 일단 결과를 저장하고, 더욱 최적화할 수 있는지 조사.
    # 설치된 공유기가 조건보다 더 많이 설치됐다면, 거리를 좀 더 벌려도 된다는 뜻 이므로 오른쪽 탐색
    if cnt >= c:
        result = mid
        start = mid + 1
    # 설치된 공유기가 조건보다 적다면 기준 거리를 너무 크게 설정했으므로, 거리의 왼쪽 탐색
    else:
        end = mid - 1

print(result)

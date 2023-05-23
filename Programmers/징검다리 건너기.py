# Programmers Lv.3
# 이진탐색


def solution(stones, k):
    left = 1  # 징검다리를 넘을 수 있는 최소 인원
    right = max(stones)  # 징검다리를 넘을 수 있는 최대 인원

    while left <= right:
        mid = (left + right) // 2  # 징검다리를 건너려는 사람의 수
        cnt = 0  # mid보다 작거나 같은 값을 가진 연속적인 돌의 수를 확인

        for stone in stones:
            if stone - mid <= 0:  # mid보다 작거나 같은 값을 가진 연속적인 돌의 수를 확인
                cnt += 1
                if cnt >= k:  # 건너는 사람(mid)보다 작은 값을 가진 "연속적인" 돌의 수가 K개 이상이면 불가능
                    break
            else:
                cnt = 0  # "연속적인" 돌의 수를 확인하기 위해 mid보다 큰 값을 가진 돌이 중간에 껴있다면 cnt를 0으로 초기화

        if cnt >= k:  # 건너는 사람의 수보다 작은 값을 가진 연속되는 돌의 개수가 k 이상이면
            # 건너려는 사람의 수가 너무 많은거니까 줄이기
            right = mid - 1
        else:
            left = mid + 1

    return left

def solution(n, times):
    answer = 0
    min_time = times[0]
    max_time = max(times) * n
    while min_time <= max_time:
        people = 0
        mid = (min_time + max_time) // 2
        for time in times:
            people += mid // time
        if people >= n:
            answer = mid
            max_time = mid - 1
        else:
            min_time = mid + 1
    return answer

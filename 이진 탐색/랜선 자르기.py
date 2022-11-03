# 파라메트릭 서치
k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
lan.sort()


def binary_search(arr, target, start, end):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        temp = 0
        for i in range(len(arr)):
            temp += arr[i] // mid
        if temp >= target:
            answer = max(answer, mid)
            start = mid + 1
        else:
            end = mid - 1
    return answer


print(binary_search(lan, n, 1, lan[-1]))

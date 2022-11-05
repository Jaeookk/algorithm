def bisect_right(arr, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid
        else:
            start = mid + 1
    return end


def bisect_left(arr, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start


if __name__ == "__main__":
    t = int(input())
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))

    # 부 배열의 모든 조합 구하기
    sumA, sumB = [], []

    for i in range(n):
        tmp = A[i]
        sumA.append(tmp)
        for j in range(i + 1, n):
            tmp += A[j]
            sumA.append(tmp)

    for i in range(m):
        tmp = B[i]
        sumB.append(tmp)
        for j in range(i + 1, m):
            tmp += B[j]
            sumB.append(tmp)
    sumB.sort()

    cnt = 0
    for i in range(len(sumA)):
        target = t - sumA[i]
        r = bisect_right(sumB, target, 0, len(sumB))
        l = bisect_left(sumB, target, 0, len(sumB))
        cnt += r - l
    print(cnt)

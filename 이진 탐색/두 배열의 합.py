def bisect_right(arr, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > target:  # mid 값이 target보다 크다면
            # mid의 인덱스 값이 target이 들어가야할 자리일 수도 있다. 그러므로 end를 mid로 내린다.
            end = mid
        else:  # mid 값이 target보다 작거나 같다면
            start = mid + 1  # start를 점점 올린다.
    return end


def bisect_left(arr, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < target:  # mid 값이 target보다 작다면
            start = mid + 1
        else:  # mid 값이 target보다 크거나 같다면
            end = mid  # end를 mid로 내리면서 가장 왼쪾의 target값으로 end를 옮긴다. 이후 start는 line 14,15에 의해 점점 end쪽으로 올라온다.
    return start  # start와 end가 겹치면 start 반환.


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

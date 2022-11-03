# a[i] + a[j] + a[k] = a[l]을 만족하는 a[l] 중에서 최대값
# 1. O(N^4) 풀이 : i,j,k,l에 대한 4중 for문 (x)
# 2. O(N^3logN) 풀이 : i,j,k 3중 for문, a[i] + a[j] + a[k]가 배열 a에 있는지 이분탐색 (x)
# 3. 미리 a에서 두 원소의 합을 다 묶어놓은 배열 two를 만든다.
#    two[m] + a[k] = a[l] 을 만족하는 a[l] 중에서 최댓값.
#    O(N^2logN) -> k,l 2중 for문, a[l] - a[k] 가 배열 two에 있는지 이분탐색
#    two의 길이는 N^2이고, log(N^2)은 2log(N) 이므로 O(N^2log(N^2)) = O(N^2 * 2logN)


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


if __name__ == "__main__":

    n = int(input())
    arr = [int(input()) for _ in range(n)]
    arr.sort()  # arr이 정렬이 된줄 알았는데 아니었음....

    two = []
    for i in range(n):
        for j in range(i, n):
            two.append(arr[i] + arr[j])
    two.sort()

    flag = False
    for i in range(n - 1, -1, -1):
        for j in range(0, i):
            target = arr[i] - arr[j]
            if binary_search(two, target, 0, len(two)):
                print(arr[i])
                flag = True
                break
        if flag:
            break

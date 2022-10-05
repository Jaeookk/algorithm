# 참고 https://jason9319.tistory.com/113햐
def binary_search(target):
    left = 0
    right = len(dp) - 1

    while left < right:
        mid = (left + right) // 2
        if dp[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right


n = int(input())
array = list(map(int, input().split()))

dp = [array[0]]

for i in range(len(array)):
    if dp[-1] < array[i]:
        dp.append(array[i])
    else:
        dp[binary_search(array[i])] = array[i]
print(dp)
print(len(dp) - 1)


# 1. 현재 위치(i)가 이전 위치의 원소들보다 크면 dp에 추가한다.
# 2. 현재 위치(i)가 이전 위치의 원소보다 작거나 같으면, 이분탐색으로 이전 위치의 원소 중 가장 큰 원소의 index값을 구한다. 그리고 dp의 index 원소를 array[i]로 바꿔준다.

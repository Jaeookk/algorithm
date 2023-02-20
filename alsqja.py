#### 1번
def solution(office, k):
    answer = 0
    L = len(office)
    for i in range(L - k + 1):
        for j in range(L - k + 1):
            sum = 0
            for x in range(k):
                for y in range(k):
                    if office[i + x][j + y] == 1:
                        sum += 1
            answer = max(answer, sum)

    return answer


print(solution([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 1, 0]], 2))
print(solution([[1, 0, 0], [0, 0, 1], [1, 0, 0]], 2))


#### 3번
import sys


def solution(n):
    x = int(n**0.5)
    dp = [sys.maxsize] * (x + 1)

    for max_start in range(x, 0, -1):
        cnt = 0
        tmp = n
        for j in range(max_start, 0, -1):
            while tmp >= j**2:
                tmp -= j**2
                cnt += 1
            if tmp == 0:
                break
        dp[max_start] = cnt
    print(dp)
    print(min(dp))


solution(15)

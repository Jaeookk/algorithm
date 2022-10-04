import sys

# 원시적인 코드로는 시간 초과가 발생할 수 있다.
# d[i] = a[1] + a[2] + ... + a[i]
# d[i] = d[i-1] + a[i]

# a[i] + a[i+1] + ... + a[j]
# = (a[1] + a[2] + ... + a[j]) - (a[1] + a[2] + ... + a[i-1])
# = d[j] - d[i-1]

n, m = map(int, sys.stdin.readline().split())
nums = [0] + list(map(int, sys.stdin.readline().split()))


def main():
    d = [0] * (n + 1)
    d[1] = nums[1]
    for i in range(2, n + 1):
        d[i] = d[i - 1] + nums[i]

    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())
        print(d[j] - d[i - 1])


if __name__ == "__main__":
    main()

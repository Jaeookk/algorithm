n = int(input())
arr = list(map(int, input().split()))


def main():
    for i in range(1, n):
        arr[i] = max(arr[i], arr[i - 1] + arr[i])

    print(max(arr))


# 10 6 9 10 15 16 -19 12 33 32

# 2 3 -1 3 7 3 9 14 9 10

if __name__ == "__main__":
    main()

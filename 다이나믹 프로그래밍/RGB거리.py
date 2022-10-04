n = int(input())

money = [[0]] + [list(map(int, input().split())) for _ in range(n)]


def main():
    d = [[0, 0, 0] for _ in range(n + 1)]
    d[1][0] = money[1][0]
    d[1][1] = money[1][1]
    d[1][2] = money[1][2]
    for i in range(2, n + 1):
        d[i][0] = min(d[i - 1][1], d[i - 1][2]) + money[i][0]
        d[i][1] = min(d[i - 1][0], d[i - 1][2]) + money[i][1]
        d[i][2] = min(d[i - 1][1], d[i - 1][0]) + money[i][2]
    print(min(d[n]))


if __name__ == "__main__":
    main()

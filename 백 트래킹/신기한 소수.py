N = int(input())


def solve(t):
    # 소수 체크 #
    flag = True
    i = 2
    while i * i <= t:
        if t % i == 0:
            flag = False
            break
        i += 1

    if flag:  # 소수가 참일 때 현재 소수 * 10 + i를 하여 다시 체크
        for i in range(1, 10):
            solve(t * 10 + i)
    else:
        return

    # N자리가 될 때 출력
    if len(str(t)) == N:
        print(t)
        return


for i in range(2, 10):
    solve(i)

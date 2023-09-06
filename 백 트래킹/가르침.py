import sys


def dfs(start, cnt):
    global ans

    if cnt == k - 5:  # 5개 글자(a, c, i, n, t)는 이미 배웠음
        tmp = 0
        for word in words:
            can_read = True # 배운 글자로 해당 단어를 읽을 수 있는지 확인
            for alpha in word:
                if not check[ord(alpha) - ord('a')]:
                    can_read = False
                    break
            # 해당 단어를 읽을 수 있는 경우
            if can_read:
                tmp += 1
        ans = max(ans, tmp)
        return
    
    for i in range(start, 26):
        if not check[i]:    # i번째 글자를 가르치지 않았다면
            check[i] = True
            dfs(i, cnt + 1)
            check[i] = False


if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().split())

    words = [set(input().rstrip()) for _ in range(n)]
    check = [False] * 26
    ans = 0

    # 가르칠 글자의 수가 5(a, n, t, i, c)보다 작은 경우
    if k < 5:
        print(0)
        exit(0)
    # 가르칠 글자의 수가 26인 경우
    elif k == 26:
        print(n)
        exit(0)

    # a, c, i, n, t 는 무조건 배워야 함
    for alpha in ('a', 'c', 'i', 'n', 't'):
        check[ord(alpha) - ord('a')] = True

    dfs(0, 0)
    print(ans)
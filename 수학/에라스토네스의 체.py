# BOJ 2960
N, K = map(int, input().split())

cheak = [False for _ in range(N + 2)]
cnt = 0
for i in range(2, N + 1):
    if cheak[i] == False:
        for j in range(i, N + 1, i):
            if cheak[j] == False:
                cheak[j] = True
                cnt += 1

                if cnt == K:
                    print(j)
                    break

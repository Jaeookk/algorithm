def rotate(G, dir):
    if dir == -1:
        tmp = G[0]
        G = G[1:] + tmp
    elif dir == 1:
        tmp = G[-1]
        G = tmp + G[:-1]
    return G


def left_gear(now, l, dir):
    if l < 0:
        return
    if gear[now][6] != gear[l][2]:
        left_gear(l, l - 1, -dir)
        gear[l] = rotate(gear[l], -dir)


def right_gear(now, r, dir):
    if r > 3:
        return
    if gear[now][2] != gear[r][6]:
        right_gear(r, r + 1, -dir)
        gear[r] = rotate(gear[r], -dir)


if __name__ == "__main__":
    gear = [input() for _ in range(4)]  # 2, 6 번째 index가 맞물림.
    k = int(input())

    for _ in range(k):
        n_gear, dir = map(int, input().split())
        left_gear(n_gear - 1, n_gear - 2, dir)
        right_gear(n_gear - 1, n_gear, dir)
        gear[n_gear - 1] = rotate(gear[n_gear - 1], dir)

    answer = 0
    for i in range(4):
        if gear[i][0] == "1":
            answer += 2**i

    print(answer)

a, b, c = map(int, input().split())


def func(x, y, z):
    if y == 1:
        return x % z
    val = func(x, y // 2, z)
    val = val * val % z
    if y % 2 == 0:
        return val
    return val * x % z


print(func(a, b, c))

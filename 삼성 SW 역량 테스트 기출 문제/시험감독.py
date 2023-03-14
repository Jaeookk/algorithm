n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
ret = 0

for i in range(n):
    if a[i] > b:
        div, mod = divmod((a[i] - b), c)
        if mod == 0:
            ret += div + 1
        else:
            ret += div + 2
    else:
        ret += 1
print(ret)

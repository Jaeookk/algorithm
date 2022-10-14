def func(n):
    if n == 1:
        return ["*"]
    stars = func(n // 3)
    L = []

    for star in stars:
        L.append(star * 3)
    for star in stars:
        L.append(star + " " * (n // 3) + star)
    for star in stars:
        L.append(star * 3)
    return L


n = int(input())
array = func(n)
for i in array:
    print("".join(i))

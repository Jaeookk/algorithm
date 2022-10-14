def func(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]
    stars = func(n // 2)
    L = []

    for i, star in enumerate(stars):
        L.append(" " * len(stars) + star + " " * len(stars))
    for i, star in enumerate(stars):
        # L.append(star + " " * ((len(stars) - i) * 2 - 1) + star)
        L.append(star + " " + star)
    return L


n = int(input())
array = func(n)
for i in array:
    print("".join(i))

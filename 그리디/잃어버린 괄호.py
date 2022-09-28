x, *y = [sum(map(int, x.split("+"))) for x in input().split("-")]
print(x - sum(y))

n, l = map(int, input().split())

waters = [tuple(map(int, input().split())) for _ in range(n)]
waters.sort()
answer = 0
last = 0
for a, b in waters:
    if b + 1 < last:
        continue
    elif a <= last <= b + 1:
        length = b - last - 1
        temp = length // l
        if length % l != 0:
            temp += 1
        answer += temp
        last = last + temp * l
    elif last < a:
        length = b - a
        temp = length // l
        if length % l != 0:
            temp += 1
        answer += temp
        last = a + l * temp - 1

print(answer)

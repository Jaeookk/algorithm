# BOJ 10773

n = int(input())
s = []
for i in range(n):
    num = int(input())
    if num == 0:
        s.pop()
    else:
        s.append(num)
print(sum(s))

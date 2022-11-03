a, b = map(int, input().split())
array_A = set(map(int, input().split()))
array_B = set(map(int, input().split()))

answer = array_A - array_B

if answer:
    print(len(answer))
    print(*sorted(answer))
else:
    print(0)

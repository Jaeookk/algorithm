import sys
f = sys.stdin.readline

n = int(f())
house = list(map(int, f().split()))
house.sort()

result = house[(n - 1)//2]

print(result)

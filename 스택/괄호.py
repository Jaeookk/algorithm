# BOJ 9012
T = int(input())

def check(x):
    sum = 0
    for target in stack:
        if target == "(":
            sum += 1
        elif target == ")":
            sum -= 1
        if sum < 0:
            return False
    if sum == 0:
        return True
    return False

for i in range(T):
    stack = list(input())
    if check(stack):
        print("YES")
    else:
        print("NO")
    
# 백준 10799 실버2
import sys

input = sys.stdin.readline
n = list(map(str, input().strip()))

stack = []
res = 0


for i in range(len(n)):
    if n[i] == "(":
        stack.append("(")

    elif n[i - 1] == ")":
        stack.pop()
        res += 1

    else:
        stack.pop()
        res += len(stack)

print(res)

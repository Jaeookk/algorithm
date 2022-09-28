import sys

# 1. 양수면 최대값끼리 곱( 1은 빼야함 )
# 2. 1은 그냥 바로 더함
# 3. 음수면 음수 최소값끼리 곱
# 4. 음수가 홀수개이고 0이 있으면 음수*0 해서 음수 버리기

N = int(sys.stdin.readline().strip())
result = 0
positive = []
negative = []
for _ in range(N):
    n = int(sys.stdin.readline().strip())
    if n > 1:
        positive.append(n)
    elif n == 1:
        result += 1
    else:
        negative.append(n)

positive.sort(reverse=True)
negative.sort()

cnt = 0
temp = 0
for i in range(len(positive)):
    if cnt == 0:
        temp = positive[i]
        cnt += 1
    else:
        result += positive[i] * temp
        cnt = 0
        temp = 0
result += temp

cnt = 0
temp = 0
for i in range(len(negative)):
    if cnt == 0:
        temp = negative[i]
        cnt += 1
    else:
        result += negative[i] * temp
        cnt = 0
        temp = 0
result += temp
print(result)

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
card = list(map(int, input().split()))
card = sorted(card)

for _ in range(m):
    s = card[0] + card[1]
    card[0] = s
    card[1] = s
    card.sort()

print(sum(card))

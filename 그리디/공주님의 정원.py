N = int(input())
flowers = []
for i in range(N):
    m1, d1, m2, d2 = map(int, input().split())
    flowers.append((m1 * 100 + d1, m2 * 100 + d2))

flowers.sort(key=lambda x: (x[0], x[1]))
print(flowers)
standard = 301  # 꽃이 이어서 필 수 있는 기간 조건
end = 0
tmp = 0
count = 0

# (215, 323)
#      (228, 425)
#           (412,           605)
#                 (502, 531)
#                          (603, 615)
#                                  (615,     903)
#                                  (615,           927)
#                                    (714, 901)
#                                                (914, 1224)
#                                                  (1005, 1231)
for i in range(N):
    if end > 1130:
        break

    # 만약 i번째 꽃의 기간이 standard를 포함하고 있다면
    if flowers[i][0] <= standard and standard < flowers[i][1]:
        if tmp != standard:  # standard를 만족시키는 꽃들의 중복된 카운트를 제한하기 위한 if문
            tmp = standard
            count += 1

        # standard를 만족시키는 꽃들 중에서 가장 기간이 긴 꽃의 마지막 기간을 저장. -> 꽃의 개수가 최소가 되려면 기간이 길어야 하기 때문
        if end < flowers[i][1]:
            end = flowers[i][1]

    # 만약 i번째 꽃의 기간이 standard를 포함하지 않는다면
    elif flowers[i][0] <= end and end < flowers[i][1]:
        standard = end  # standard를 이전 꽃의 마지막 기간으로 갱신. 다음 꽃은 이전 꽃의 마지막 기간(standard) 이전에 꽃을 피워야함.
        tmp = standard  # 위의 if문에서 중복된 카운트를 제한하기 위해 tmp 갱신.
        end = flowers[i][1]  # 마지막 기간 갱신
        count += 1
    # print(i, "/", count, "/", standard, "/", end)

if end <= 1130:
    count = 0
print(count)

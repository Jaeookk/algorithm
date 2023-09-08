# 최댓값을 구하기 위해서는 덧셈 뒤에 나오는 수는 가장 커져야 하고, 뺄셈 뒤에 나오는 수는 가장 작아져야 한다.
# 따라서 i번째 수부터 j번째 수까지, 여러 가지 가능한 연산 결과 중 (1) 최댓값과 (2) 최솟값을 각각 저장해두어야 한다.

# i < k <= j 인 k를 생각하여 [i ~ j] 구간이 [i ~ k-1], [k ~ j] 의 두 구간으로 나뉜다고 하자.
# 이 때, op[k-1]의 종류에 따라서 dp_M[i][j]와 dp_m[i][j]계산을 위해 기억해둘 값이 달라진다.

# dp_M[i][j]는 i번째 숫자 ~ j번째 숫자 까지의 최대 연산 결과
# dp_m[i][j]는 i번째 숫자 ~ j번째 숫자 까지의 최소 연산 결과

# op[k-1]이 (+)인 경우,
# 최댓값을 위해서는 dp_M[i][j] = max(dp_M[i][j], dp_M[i][k-1] + dp_M[k][j])를 실행. (큰 값과 큰 값을 더함)
# 최솟값을 위해서는 dp_m[i][j] = min(dp_m[i][j], dp_m[i][k-1] + dp_m[k][j])를 실행. (작은 값과 작은 값을 더함)

# op[k-1]이 (-)인 경우,
# 최댓값을 위해서는 dp_M[i][j] = max(dp_M[i][j], dp_M[i][k-1] - dp_m[k][j])을 실행. (큰 값에서 작은 값을 뺌)
# 최솟값을 위해서는 dp_m[i][j] = min(dp_m[i][j], dp_m[i][k-1] - dp_M[k][j])을 실행. (작은 값에서 큰 값을 뺌)

# 위 과정을 i와 j의 간격이 1일때부터 ~ 최대일때까지 모든 i와 j에 대해서 반복.


def solution(arr):
    nums = [int(x) for x in arr[::2]]
    ops = [x for x in arr[1::2]]
    dp_M = [[-1e9] * len(nums) for _ in range(len(nums))]
    dp_m = [[1e9] * len(nums) for _ in range(len(nums))]

    for i in range(len(nums)):  # dp 테이블 초기화
        dp_M[i][i] = nums[i]
        dp_m[i][i] = nums[i]

    for d in range(1, len(nums)):
        # i와 j의 간격이 1일때부터 차례대로 조사.

        for i in range(len(nums)):
            j = i + d
            if j >= len(nums):
                continue

            for k in range(i + 1, j + 1):  # i < k <= j 일때
                # ops[k-1]은 nums[k-1]과 nums[k]의 연산자에 해당.
                # print(f"i : {i}, k : {k}, j : {j}")

                if ops[k - 1] == "+":
                    dp_M[i][j] = max(dp_M[i][j], dp_M[i][k - 1] + dp_M[k][j])
                    dp_m[i][j] = min(dp_m[i][j], dp_m[i][k - 1] + dp_m[k][j])
                else:
                    dp_M[i][j] = max(dp_M[i][j], dp_M[i][k - 1] - dp_m[k][j])
                    dp_m[i][j] = min(dp_m[i][j], dp_m[i][k - 1] - dp_M[k][j])

    return dp_M[0][len(nums) - 1]

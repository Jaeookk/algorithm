a, b, c = map(int, input().split())


def pow(x, y, z):
    if y == 1:
        return x % z
    val = pow(x, y // 2, z)
    val = val * val % z
    if y % 2 == 0:
        return val
    return val * x % z


print(pow(a, b, c))
# 코드에서 POW 함수가 바로 a^b mod m을 계산해주는 함수이다.
# base condition은 05번째 줄에 명시. b = 1일 때를 base condition으로 뒀는데 b = 0일 때로 두어도 된다.
# 그리고 a가 m보다 클 수 있기 때문에 a를 반환하는 대신 a % m을 반환

# 절차지향적인 사고 대신 귀납적인 사고로 코드를 이해하자.
# 재귀 함수를 잘 짜려면 귀납적인 사고, 즉 base condition을 잘 잡아뒀고
# k승의 결과를 토대로 2k, 2k+1승의 결과를 계산할 수 있으니
# 마치 도미노를 쓰러트리는 것 처럼 모든 결과가 잘 계산될 것이다로 함수를 이해할 필요가 있다.
# https://blog.encrypted.gg/943?category=773649

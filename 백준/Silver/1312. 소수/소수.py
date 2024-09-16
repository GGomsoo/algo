# 24-09-14
# 소수
# 실버 V
# 런타임 에러 (indexError)

A, B, N = map(int, input().split())

for i in range(N):
    A = (A % B) * 10
    X = A // B

print(X)
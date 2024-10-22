# 가장 긴 증가하는 부분 수열
# 실버 II

N = int(input()) # 수열 A의 크기
A = list(map(int, input().split())) # 수열 A

dp = [1] * N # 모든 dp의 초기값 1

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
# 동물원
# 실버 I
## DP문제

N = int(input())
dp = [0] * 100_001
dp[0] = 1
dp[1] = 3
dp[2] = 7

for i in range(3, N+1):
    dp[i] = (2 * dp[i-1] + dp[i-2]) % 9901

print(dp[N])
# 피보나치 수 2
# 브론즈 I

N = int(input())
dp = [0] * 91

dp[0] = 0
dp[1] = 1

for i in range(2, 91):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])
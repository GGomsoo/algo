# 포도주 시식
# 실버 I

N = int(input())
dp = [0] * 10_001
wine = [0] * 10_001
for i in range(1, N+1):
    cnt = int(input())
    wine[i] = cnt

dp[1] = wine[1]
dp[2] = wine[1] + wine[2]
dp[3] = max(wine[1]+wine[3], wine[2]+wine[3], dp[2])

for j in range(4, N+1):
    dp[j] = max(dp[j-3] + wine[j-1] + wine[j], dp[j-2] + wine[j], dp[j-1])


print(dp[N])
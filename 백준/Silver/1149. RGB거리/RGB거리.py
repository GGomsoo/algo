# RGB 거리
# 실버 I

N = int(input()) # 집의 수
cost = [list(map(int, input().split())) for _ in range(N)] # 빨 초 파로 칠하는 비용

dp = [[0, 0, 0] for _ in range(1001)]

dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

for i in range(N):
    dp[i][0] = min(dp[i-1][1] + cost[i][0], dp[i-1][2] + cost[i][0])
    dp[i][1] = min(dp[i-1][0] + cost[i][1], dp[i-1][2] + cost[i][1])
    dp[i][2] = min(dp[i-1][0] + cost[i][2], dp[i-1][1] + cost[i][2])

print(min(dp[N-1]))

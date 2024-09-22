# 파도반 수열
# 실버 III

T = int(input()) # 테스트 케이스의 개수
for _ in range(T):
    N = int(input())
    dp = [0] * 101
    dp[1] = dp[2] = dp[3] = 1 # 처음 3개의 삼각형 변의 길이는 같다

    for i in range(4, N+1):
        dp[i] = dp[i-3] + dp[i-2] # 규칙 발견
    
    print(dp[N])
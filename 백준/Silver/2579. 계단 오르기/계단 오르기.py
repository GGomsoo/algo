# 계단 오르기
# 실버 III
# 연속 3계단은 안된다

N = int(input()) # 계단의 갯수
stairs = [0] * 301 # 시작점은 계단에 포함되지 않는다. 계단의 개수는 300이하
dp = [0] * 301

for i in range(1, N+1): # 계단에 적힌 점수들을 등록
    stair_point = int(input())
    stairs[i] = stair_point
    

dp[1] = stairs[1] # 첫 번째 계단
dp[2] = stairs[1] + stairs[2] # 1번, 2번 계단 밟고간 경우
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3]) # 2칸 건너뛴 경우 중 큰 값으로

for i in range(4, N+1):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i]) 

print(dp[N])
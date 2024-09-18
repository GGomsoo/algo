# 평범한 배낭
# 골드 V
'''
4 7
6 13
4 8
3 6
5 12
'''

N, K = map(int, input().split()) # 물건의 갯수 N, 넣을 수 있는 최대 무게 K
dp = [[0] * (K+1) for _ in range(N+1)]

things = [[0, 0]] # 
for _ in range(N):
    thing = list(map(int, input().split())) # 무게, 가치 순으로 입력
    things.append(thing) # 물품 리스트에 추가

for j in range(1, N+1): # 물건 번호도 1번 부터
    for i in range(1, K+1): # 무게는 1부터
        weight = things[j][0]
        value = things[j][1]

        if i < weight: # 가방 공간보다 물건이 더 무거운 경우
            dp[j][i] = dp[j-1][i]
        else: # 가방에 물건 넣을 수 있는 경우
            # 이전 가방의 가치, 새로운 물건을 넣은 경우의 가치 중 더 큰 값을 할당
            dp[j][i] = max(dp[j-1][i], dp[j-1][i-weight] + value)

print(dp[N][K])
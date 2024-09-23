# 내려가기
# 골드 V

## 메모리 초과, 정답은 나옴
# N = int(input())
# score = [list(map(int, input().split())) for _ in range(N)]

# min_dp = [[0,0,0] for _ in range(10001)]
# max_dp = [[0,0,0] for _ in range(10001)]

# min_dp[0] = score[0]
# max_dp[0] = score[0]

# for i in range(1, N):
#     min_dp[i][0] = min(min_dp[i-1][0] + score[i][0], min_dp[i-1][1] + score[i][0])
#     min_dp[i][1] = min(min_dp[i-1]) + score[i][1]
#     min_dp[i][2] = min(min_dp[i-1][1] + score[i][2], min_dp[i-1][2] + score[i][2])

#     max_dp[i][0] = max(max_dp[i-1][0] + score[i][0], max_dp[i-1][1] + score[i][0])
#     max_dp[i][1] = max(max_dp[i-1]) + score[i][1]
#     max_dp[i][2] = max(max_dp[i-1][1] + score[i][2], max_dp[i-1][2] + score[i][2])

# print(max(max_dp[N-1]), min(min_dp[N-1]))

N = int(input())
score = list(map(int, input().split()))

## DP에서의 슬라이딩 윈도우 기법은
## 메모이제이션을 할 때 더이상 사용하지 않는 값을 저장하지 않고 배열을 계속하여 갱신
## 앞으로 쓰이지 않을 값이 메모이제이션 되지 않음 -> 배열 최소한의 상태로 유지 -> 메모리 감소
min_dp = score
max_dp = score

for i in range(N-1):
    A, B, C = map(int, input().split())

    min_dp = [min(A + min_dp[0], A + min_dp[1]), (min(min_dp) + B), min(C + min_dp[1], C + min_dp[2])]
    max_dp = [max(A + max_dp[0], A + max_dp[1]), (max(max_dp) + B), max(C + max_dp[1], C + max_dp[2])]

print(max(max_dp), min(min_dp))
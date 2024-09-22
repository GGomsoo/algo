# IOIOI
# 실버 I

N = int(input())
M = int(input())
S = input()
# P = "IOI" + "OI" * (N-1)
# ans = 0

# for i in range(M):
#     if S[i:i+len(P)] == P:
#         ans += 1

# print(ans)

P = "IOI"

ans = idx = cnt = 0
while idx < M-1: # S의 인덱스 내에서
    if S[idx:idx+3] == P: # 3자리씩 비교해서 P가 맞으면
        idx += 2 # 2칸 전진
        cnt += 1 # P의 갯수 카운팅

        if cnt == N: # P의 갯수가 N과 맞다면
            ans += 1 # 정답 카운팅
            cnt -= 1 # P의 갯수를 -1 한다.
    
    else:
        idx += 1 # P가 아니라면 한 칸 전진
        cnt = 0 # P의 카운팅 = 0

print(ans)
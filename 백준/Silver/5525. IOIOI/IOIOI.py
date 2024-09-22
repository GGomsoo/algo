# IOIOI
# 실버 I

N = int(input())
M = int(input())
S = input()
P = "IOI" + "OI" * (N-1)
ans = 0

for i in range(M):
    if S[i:i+len(P)] == P:
        ans += 1

print(ans)
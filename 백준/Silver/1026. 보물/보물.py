# 보물
# 실버 IV
# S = A[0] * B[0] + ... + A[N-1] * B[N-1]
# S의 최솟값 구하기
# 오름차순, 내림차순 하여 두 배열의 숫자를 각각 곱한 후 누적

N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()), reverse=True)

ans = 0
for i in range(N):
    ans += A[i] * B[i]

print(ans)
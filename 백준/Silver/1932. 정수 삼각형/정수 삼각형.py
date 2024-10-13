# 정수 삼각형
# 실버 I
# DP 문제

N = int(input())

triangle = []
for _ in range(N):
    numbers = list(map(int, input().split()))
    triangle.append(numbers)

for j in range(1, N):
    for i in range(j+1):
        if i == 0:
            triangle[j][i] += triangle[j-1][i]
        elif i == j:
            triangle[j][i] += triangle[j-1][i-1]
        else:
            triangle[j][i] += max(triangle[j-1][i-1], triangle[j-1][i])

print(max(triangle[N-1]))
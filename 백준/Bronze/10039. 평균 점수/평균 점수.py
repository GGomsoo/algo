# 평균 점수
# 브론즈 IV

N = 5

total = 0
for _ in range(N):
    score = int(input())
    if score < 40:
        score = 40
    total += score

print(total // N)

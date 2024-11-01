# 민주주의 - 마라톤 문제
# 브론즈 IV

N, M = map(int, input().split()) # 문제의 수 N, 출제위원의 수 M
A = [list(input()) for _ in range(N)]

result = 0
for j in range(N):
    agree_cnt = 0
    for i in range(M):
        if A[j][i] == "O":
            agree_cnt += 1
    
    if agree_cnt > M // 2:
        result += 1

print(result)
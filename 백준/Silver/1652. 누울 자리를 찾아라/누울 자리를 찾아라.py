# 누울 자리를 찾아라
# 실버 V
# 연속 2칸 이상의 빈 칸 있는 경우를 구하자

N = int(input())
rooms = [list(input()) for _ in range(N)]

# 가로
row = 0
for j in range(N):
    temp_row = 0
    for i in range(N):
        if rooms[j][i] == ".": # 빈 공간인 경우
            temp_row += 1
        else: # 짐이 있는 경우
            if temp_row >= 2:
                row += 1
            temp_row = 0
    if temp_row >= 2: # 짐이 없고, 다 빈 공간인 경우
        row += 1

# 세로
col = 0
for j in range(N):
    temp_col = 0
    for i in range(N):
        if rooms[i][j] == ".": # 빈 공간인 경우
            temp_col += 1
        else: # 짐이 있는 경우
            if temp_col >= 2: # 이미 누울자리 조건을 만족했다면
                col += 1 # 누울 수 있는 자리의 개수 추가
            temp_col = 0 # 변수 초기화
    if temp_col >= 2: # 짐이 없고, 다 빈 공간인 경우
        col += 1

print(row, col)
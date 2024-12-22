C, R = map(int, input().split())
K = int(input())
hall = [[0] * C for _ in range(R)]

if K > C * R:
    print(0)
    exit(0)

# 상, 우, 하, 좌 순서로 변경
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

i = R-1  # 좌측 하단 시작
j = 0
direction = 0

for S in range(1, C * R + 1):
    hall[i][j] = S
    
    if S == K:
        print(j+1, R-i)  # 좌표계 변환
        break

    ni = i + di[direction]
    nj = j + dj[direction]

    if ni < 0 or ni >= R or nj < 0 or nj >= C or hall[ni][nj] != 0:
        direction = (direction + 1) % 4
        ni = i + di[direction]
        nj = j + dj[direction]
    
    i, j = ni, nj
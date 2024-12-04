# 미세먼지 안녕!
# 골드 IV

# 미세먼지 확산
def dust():
    diffusion_dust = [[0] * C for _ in range(R)]
    
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    for i in range(R):
        for j in range(C):
            if room_info[i][j] != -1 and room_info[i][j] != 0:
                cnt = 0

                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]

                    if 0 <= ni < R and 0 <= nj < C and (ni, nj) not in cleaner:
                        cnt += 1
                        diffusion_dust[ni][nj] += room_info[i][j] // 5
                
                room_info[i][j] = room_info[i][j] - (room_info[i][j] // 5) * cnt
    
    for i in range(R):
        for j in range(C):
            room_info[i][j] += diffusion_dust[i][j]


# 공기청정기 작동(상단)
def air_top():
    global top_cleaner
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    start_i, start_j = top_cleaner, 1
    direction = 0
    prev = 0

    while True:
        ni = start_i + di[direction]
        nj = start_j + dj[direction]

        if start_i == top_cleaner and start_j == 0:
            break

        if not (0 <= ni < R and 0 <= nj < C):
            direction = (direction + 1) % 4
            continue

        room_info[start_i][start_j], prev = prev, room_info[start_i][start_j]
        start_i = ni
        start_j = nj


# 공기청정기 작동(하단)
def air_bottom():
    global bottom_cleaner
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    start_i, start_j = bottom_cleaner, 1
    direction = 0
    prev = 0

    while True:
        ni = start_i + di[direction]
        nj = start_j + dj[direction]

        if start_i == bottom_cleaner and start_j == 0:
            break

        if not (0 <= ni < R and 0 <= nj < C):
            direction = (direction + 1) % 4
            continue

        room_info[start_i][start_j], prev = prev, room_info[start_i][start_j]
        start_i = ni
        start_j = nj
    

R, C, T = map(int, input().split())
room_info = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치정보
cleaner = [(i, 0) for i in range(R) if room_info[i][0] == -1]
top_cleaner = cleaner[0][0]
bottom_cleaner = cleaner[1][0]

for _ in range(T):
    dust()
    air_top()
    air_bottom()

# 남은 미세먼지의 총합을 계산
result = 0
for i in range(R):
    for j in range(C):
        if room_info[i][j] > 0:
            result += room_info[i][j]
print(result)
# 마법사 상어와 비바라기
# 골드 V

# 격자의 크기, 이동 명령의 수
N, M = map(int, input().split())

# 격자에 대한 정보
boards = [list(map(int, input().split())) for _ in range(N)]

# 이동 명령에 대한 정보
move_commands = [tuple(map(int, input().split())) for _ in range(M)]

# 구름의 초기 좌표
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

# 이동 명령에 대한 방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 이동 명령에 대해
for d, s in move_commands:

    # 구름의 움직임에 대해
    move_clouds = []
    for x, y in clouds:
        # 격자는 이어져있기 때문에, 이동 위치가 격자의 크기를 넘어설 경우, N으로 나누어준다
        new_x = (x + dx[d-1] * s) % N
        new_y = (y + dy[d-1] * s) % N

        # 이동한 칸의 바구니에 물의 양 1 증가 및 위치정보 추가
        boards[new_x][new_y] += 1
        move_clouds.append((new_x, new_y))
    
    # 이동이 완료된 구름들에 대해
    for move_x, move_y in move_clouds:
        basket = 0

        # 대각선 네방향 탐색
        dmx = [-1, -1, 1, 1]
        dmy = [-1, 1, 1, -1]

        for k in range(4):
            new_mx = move_x + dmx[k]
            new_my = move_y + dmy[k]

            # 이번엔 격자의 경계를 벗어나선 안된다
            if 0 <= new_mx < N and 0 <= new_my < N:
                # 대각선 위치에 물이 있는 경우 바구니의 수 1 추가
                if boards[new_mx][new_my]:
                    basket += 1
        
        # 바구니의 수 만큼 물의 양 증가
        boards[move_x][move_y] += basket
    
    # 새로운 구름 생성에 대해
    new_clouds = []
    for i in range(N):
        for j in range(N):
            # 해당 위치가, 이전에 구름이 있던곳이 아니고, 물의 양이 2 이상인 경우
            if (i, j) not in move_clouds and boards[i][j] >= 2:
                # 물의 양을 2 감소, 해당 위치에 구름 생성
                boards[i][j] -= 2
                new_clouds.append((i, j))
    
    # 기존의 구름에 대한 정보를 갱신
    clouds = new_clouds

# 모든 이동이 끝난 후 바구니에 들어있는 물의 양
result = 0
for i in range(N):
    for j in range(N):
        # 해당 바구니에 물이 있으면, 물의 양만큼 결과값에 추가
        if boards[i][j]:
            result += boards[i][j]

print(result)
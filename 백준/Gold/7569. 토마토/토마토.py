# 토마토
# 골드 V

from collections import deque

def tomato():
    q = deque()

    # 상자를 쌓아두기 때문에 3차원으로 탐색
    # 토마토의 위치를 q에 넣는다
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if box[z][y][x] == 1:
                    q.append((z, y, x))
    
    while q:
        z, y, x = q.popleft()

        # 6방향 탐색 (위 아래 상 우 하 좌)
        dz = [-1, 1, 0, 0, 0, 0]
        dy = [0, 0, -1, 0, 1, 0]
        dx = [0, 0, 0, 1, 0, -1]

        for k in range(6):
            nz = z + dz[k]
            ny = y + dy[k]
            nx = x + dx[k]

            # 상자 범위 내에 있고 안 익은 토마토라면
            # 주변 토마토의 영향을 받아 익게 만든다
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                if box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = box[z][y][x] + 1
                    q.append((nz, ny, nx))


M, N, H = map(int, input().split()) # 가로, 세로, 상자 갯수
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
tomato_time = 0 # 토마토 다 익는데 걸리는 시간

tomato()

for tmt_box in box: # 층층이 쌓아둔 상자 하나를 갖고온다
    for tmt in tmt_box: # 층층이 쌓아둔 상자 하나를 갖고온다
        if 0 in tmt: # 안 익은 토마토가 있다면 -1을 출력하고 종료한다
            print(-1)
            exit(0)
        tomato_time = max(tomato_time, *tmt)
print(tomato_time - 1)
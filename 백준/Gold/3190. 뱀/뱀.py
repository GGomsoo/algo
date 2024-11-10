# 뱀
# 골드 IV
# 빈칸 0 / 뱀 3 / 사과 5
from collections import deque

def move_snake(j, i):
    global cnt, D

    boards[j][i] = 3
    snakes = deque([(j, i)])

    while snakes:
        cnt += 1

        dj = [-1, 0, 1, 0]
        di = [0, 1, 0, -1]

        nj = snakes[-1][0] + dj[D]
        ni = snakes[-1][1] + di[D]

        # 새로운 이동반경이 게임판 내에 있으면서 뱀의 몸통이 아닌 경우
        if 0 <= nj < N and 0 <= ni < N and boards[nj][ni] != 3:
            # 해당 위치에 사과가 있는 경우
            if boards[nj][ni] == 5:
                # 뱀의 몸 길이 늘어난다
                boards[nj][ni] = 3
                snakes.append((nj, ni))
            
            # 빈칸의 경우
            elif boards[nj][ni] == 0:
                # 해당 칸으로 뱀의 머리가 이동
                boards[nj][ni] = 3
                snakes.append((nj, ni))

                # 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다
                y, x = snakes.popleft()
                boards[y][x] = 0

            # 방향 전환
            if cnt in direction_info:
                if direction_info[cnt] == "L":
                    D = (D - 1) % 4
                else:
                    D = (D + 1) % 4

        # 범위 내에 없다 or 몸과 부딪혔다
        else:
            # 게임 종료
            break

N = int(input())
boards = [[0] * N for _ in range(N)]

# 사과에 대한 정보
K = int(input())
for _ in range(K):
    r, c = map(int, input().split()) # 사과의 위치 행, 열
    boards[r-1][c-1] = 5 # 사과를 5로 설정

# 방향 변환에 대한 정보
L = int(input())
direction_info = {}
for _ in range(L):
    sec, direction = input().split()
    direction_info[int(sec)] = direction

cnt = 0
D = 1

move_snake(0, 0)
print(cnt)
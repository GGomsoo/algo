# 아기 상어
# 골드 III

from collections import deque

def baby_shark_hunting(i, j):
    global baby_shark_weight
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    baby_shark = deque([(i, j)])
    hunting_possible = []

    while baby_shark:
        i, j = baby_shark.popleft()

        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N:
                # 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없다.
                # 크기가 같은 물고기는 먹을 수 없지만, 그 칸은 지나갈 수 있다.
                if not visited[ni][nj] and baby_shark_weight >= aqaurium[ni][nj]:
                    visited[ni][nj] = visited[i][j] + 1
                    baby_shark.append((ni, nj))

                    # 자신의 크기보다 작은 물고기만 먹을 수 있다.
                    if aqaurium[ni][nj] != 0 and baby_shark_weight > aqaurium[ni][nj]:
                        hunting_possible.append((visited[ni][nj] - 1, ni, nj))
    
    # 거리가 가장 가까운 물고기
    # 가장 위에 있는 물고기
    # 가장 왼쪽에 있는 물고기 순으로 먹는다
    hunting_possible.sort(key=lambda x: (x[0], x[1], x[2]))
    return hunting_possible

N = int(input())
aqaurium = [list(map(int, input().split())) for _ in range(N)]
baby_shark_weight = 2
baby_shark_eat_cnt = 0
ans = 0

# 아기상어 위치 포착
for i in range(N):
    for j in range(N):
        if aqaurium[i][j] == 9:
            shark_i, shark_j = i, j
            aqaurium[i][j] = 0
            break

# 물고기를 먹은 자리를 아기상어의 자리로 갱신
# 그 위치에서 다시 먹을 수 있는 물고기를 탐색
while True:
    fish_list = baby_shark_hunting(shark_i, shark_j)

    if not fish_list:
        print(ans)
        break

    time, shark_i, shark_j = fish_list.pop(0)
    baby_shark_eat_cnt += 1
    ans += time
    aqaurium[shark_i][shark_j] = 0

    if baby_shark_weight == baby_shark_eat_cnt:
        baby_shark_weight += 1
        baby_shark_eat_cnt = 0
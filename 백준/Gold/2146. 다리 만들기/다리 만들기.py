from collections import deque
import sys; input = sys.stdin.readline

N = int(input()) # 나라의 크기

world = [list(map(int, input().split())) for _ in range(N)] # 지도
change = 2 # 섬을 구분하기 위한 초기값
min_num = float('inf') # 최소값 초기값

# 섬 구분하기
# 지도에 모두 1로 표시된 섬들을 각각 다른값으로 변경하여 섬을 구분
def change_land(i, j):
    world[i][j] = change # 해당 좌표의 섬을 구분값으로 변경
    q = deque([(i, j)])

    while q:
        i, j = q.popleft()

        di = [0, 1, 0, -1]
        dj = [-1, 0, 1, 0]

        for k in range(4): # 네방향 탐색
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N: # 신규 좌표가 범위 내에 있다면
                if world[ni][nj] == 1: # 신규 좌표의 값이 1이라면
                    world[ni][nj] = change # 구분값으로 변경
                    q.append((ni, nj))

# 섬에 다리놓기
def bfs(land):
    q = deque([]) # 섬의 좌표를 넣을 q
    dist = [[0] * N for _ in range(N)] # 거리계산
    visited = [[0] * N for _ in range(N)] # 방문체크

    for i in range(N):
        for j in range(N):
            if world[i][j] == land: # 해당 섬의 값이 for 문에서 받은 변수값이라면
                q.append((i, j)) # q에 해당 좌표를 삽입
                dist[i][j] = 1 # 거리 1 시작

    while q:
        i, j = q.popleft()

        di = [0, 1, 0, -1]
        dj = [-1, 0, 1, 0]

        for k in range(4): # 네방향 탐색
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N: # 신규 좌표가 범위 내에 있으면서
                if world[ni][nj] and world[ni][nj] != land: # 해당 지역이 바다가 아니면서, 다른 섬을 만났을 경우
                    return dist[i][j] - 1 # 해당 섬까지 가는데 이은 다리의 개수를 반환한다

                if not visited[ni][nj] and not world[ni][nj]: # 방문한 적 없고, 해당 지역이 바다라면
                    visited[ni][nj] = 1 # 방문표시
                    dist[ni][nj] = dist[i][j] + 1 # 다리를 1개 놓는다
                    q.append((ni, nj))

# 1로 되어있는 섬들을 각각 다른 값으로 구분
for i in range(N):
    for j in range(N):
        if world[i][j] == 1:
            change_land(i, j)
            change += 1

for w in range(2, change):
    min_num = min(min_num, bfs(w))

print(min_num)
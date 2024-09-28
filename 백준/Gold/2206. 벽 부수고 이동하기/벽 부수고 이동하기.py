# 벽 부수고 이동하기
# 골드 III
## 틀리고 이후에 구글에서 찬스 봤다..

from collections import deque

def bfs(j, i, wall_cnt):
    visited[j][i][wall_cnt] = 1
    q = deque([(j, i, wall_cnt)])

    while q:
        j, i, wall_cnt = q.popleft()

        if (j, i) == (N-1, M-1):
            return visited[j][i][wall_cnt]
        
        # 네방향 탐색
        dj = [-1, 0, 1, 0]
        di = [0, 1, 0, -1]

        for k in range(4):
            nj = j + dj[k]
            ni = i + di[k]

            # 신규 좌표가 지도 내에 있으면서
            if 0 <= nj < N and 0 <= ni < M:
                # 해당 위치가 벽이면서, 벽 부술 기회가 있고, 방문한 적 없다면
                if maps[nj][ni] == 1 and wall_cnt and not visited[nj][ni][0]:
                    # 벽 부수고 이동한다
                    visited[nj][ni][0] = visited[j][i][wall_cnt] + 1
                    # Q에는 새로운 좌표와, 벽 부술 기회가 없다는 의미의 0을 넣는다.
                    q.append((nj, ni, 0))
                
                # 빈 공간이고, 방문한 적 없다면
                elif maps[nj][ni] == 0 and not visited[nj][ni][wall_cnt]:
                    # 방문처리 한다.
                    visited[nj][ni][wall_cnt] = visited[j][i][wall_cnt] + 1
                    q.append((nj, ni, wall_cnt))
    
    # 최종 목적지에 도달 할 수 없다면 -1을 출력한다.
    return -1

N, M = map(int, input().split()) # 세로 N, 가로 M
maps = [list(map(int, input())) for _ in range(N)] # 지도를 그린다.
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)] # (이동거리, 벽 파괴 여부) 체크할 3차원 배열

print(bfs(0, 0, 1)) # y좌표, x좌표, 벽 파괴가능 횟수
# 아기 상어 2
# 실버 II

from collections import deque

def baby_shark2():
    q = deque()

    # 상어의 위치를 q에 넣는다
    for j in range(N):
        for i in range(M):
            if place[j][i]:
                q.append((j, i))

    while q:
        j, i = q.popleft()

        # 8방향 탐색
        dj = [0, 1, 1, 1, 0, -1, -1, -1]
        di = [-1, -1, 0, 1, 1, 1, 0, -1]

        for k in range(8):
            nj = j + dj[k]
            ni = i + di[k]

            # 새 좌표가 공간 내에 있고
            if 0 <= nj < N and 0 <= ni < M:
                # 방문한 적 없고, 빈 공간이라면
                if not visited[nj][ni] and place[nj][ni] == 0:
                    # 거리 추가
                    visited[nj][ni] = visited[j][i] + 1
                    q.append((nj, ni))

N, M = map(int, input().split()) # 세로 N, 가로 M
place = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)] # 공간 방문체크 배열
ans = 0 # 최대 안전 거리

baby_shark2()

# 공간을 탐색하여, 빈 공간인 경우에 대한 조건문 실행
for j in range(N):
    for i in range(M):
        if place[j][i] == 0:
            ans = max(ans, visited[j][i])

print(ans)
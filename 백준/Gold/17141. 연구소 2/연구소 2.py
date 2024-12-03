# 연구소 2
# 골드 IV

from collections import deque

# 바이러스 놓을 곳 정하기
def input_virus(cnt, number):
    global result
    # 바이러스 놓을 위치 M개 골랐다면 퍼트려보자
    if cnt == M:
        # 바이러스 확산값과 결과값 중 최소값을 결과값으로 갱신
        result = min(result, spread_virus(virus_list))
        return

    # 바이러스를 골랐다 놨다
    for i in range(number, len(virus_location)):
        virus_list.append(virus_location[i])
        input_virus(cnt + 1, i + 1)
        virus_list.pop()

# 바이러스 퍼트리기
def spread_virus(selected):
    visited = [[0] * N for _ in range(N)]
    virus = deque()
    spread_time = 0

    # 선택한 정보에서 좌표 정보를 얻어온다
    # 바이러스 덱에 좌표 추가 및 방문처리
    for i, j in selected:
        virus.append((i, j))
        visited[i][j] = 1

    while virus:
        i, j = virus.popleft()
        
        # 네방향 탐색
        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            # 연구소 내에 있으면서
            # 방문한 적 없고, 벽도 아니라면
            # 방문처리, 확산시간 갱신, 바이러스 덱에 좌표 추가
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj] and lab[ni][nj] != 1:
                    visited[ni][nj] = visited[i][j] + 1
                    spread_time = max(spread_time, visited[ni][nj] - 1)
                    virus.append((ni, nj))
    
    # 다 퍼트렸는지 검토
    # 빈 칸이 하나라도 있다면 무한대를 반환
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and lab[i][j] != 1:
                return float("INF")
    
    # 확산시간 반환
    return spread_time

# 연구소 크기, 바이러스의 갯수
N, M = map(int, input().split())

# 연구소에 대한 정보
lab = [list(map(int, input().split())) for _ in range(N)]

# 바이러스를 놓을 수 있는 위치에 대한 정보
# 선택한 위치를 담을 빈 list
virus_location = [(i, j) for i in range(N) for j in range(N) if lab[i][j] == 2]
virus_list = []

# 정답 초기값을 무한대로 설정
result = float("INF")

# 바이러스 놓을 위치 고르기
input_virus(0, 0)

# 결과값이 무한대라면 -1을 출력 ( == 빈칸이 남아있다 )
# 그게 아니라면 결과값을 출력 ( 결과값이 확산시간으로 갱신되었음 )
print(result if result != float("INF") else -1)
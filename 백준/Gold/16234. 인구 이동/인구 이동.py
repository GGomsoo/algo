# 인구 이동
# 골드 IV

from collections import deque

def human_migration(j, i):
    union = [(j, i)] # 연합에 대한 정보
    visited[j][i] = 1 # 방문 처리
    total_union_people = countrys[j][i] # 국경선을 공유한 나라의 총 인구수
    q = deque([(j, i)]) # Q에 나라에 대한 좌표 입력

    while q:
        j, i = q.popleft()

        # 네방향 탐색
        dj = [-1, 0, 1, 0]
        di = [0, 1, 0, -1]

        for k in range(4):
            nj = j + dj[k]
            ni = i + di[k]

            # 땅 범위 내에 있으면서
            if 0 <= nj < N and 0 <= ni < N:
                # 방문한 적 없고, 두 나라의 인구 차이가 L이상 R이하인 경우
                if not visited[nj][ni] and (L <= abs(countrys[j][i] - countrys[nj][ni]) <= R):
                    visited[nj][ni] = 1 # 방문 처리
                    union.append((nj, ni)) # 연합에 추가
                    total_union_people += countrys[nj][ni] # 총 인구수 추가
                    q.append((nj, ni)) # Q에 좌표 추가
    
    # 연합을 이룬 각 칸의 인구수 = 총 인원수 // 연합의 수
    avg_union_people = total_union_people // len(union)
    for y, x in union: # 연합에 대한 좌표를 꺼내어
        countrys[y][x] = avg_union_people # 인구수 수정
    
    return len(union) > 1 # 연합의 수가 2 이상 == 다른 나라와 국경을 공유했다

N, L, R = map(int, input().split()) # 땅의 크기, 최소, 최대
countrys = [list(map(int, input().split())) for _ in range(N)] # 나라에 대한 정보
movement_day = 0 # 인구 이동에 걸린 시간

while True: # 인구 이동이 없을 때 까지 지속한다
    visited = [[0] * N for _ in range(N)] # 방문처리
    border_sharing = False # 국경선 공유 여부

    for j in range(N):
        for i in range(N):
            if not visited[j][i] and human_migration(j, i):
                border_sharing = True
    
    if border_sharing: # 국경을 공유했다 == 인구 이동이 있었다
        movement_day += 1 # 1일 추가
    else:
        break

print(movement_day)
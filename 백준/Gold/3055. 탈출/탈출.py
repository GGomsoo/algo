# 탈출
# 골드 IV
# . 빈곳 / * 물 / X 돌 / D 비버의 굴 / S 고슴도치
# 고슴도치가 물 피해서 비버의 굴에 무사히 도착하면 걸린 시간을 출력
# 도착 못하면 KAKTUS 를 출력

from collections import deque

def escape_forest(j, i):
    # 해당 위치 방문처리
    visited[j][i] = 1

    while q:
        j, i = q.popleft()

        # 비버의 굴 위치가 고슴도치로 변했다 = 무사히 굴에 도착했다
        # 굴까지 오는데 걸린 시간을 return 한다
        if forest[fj][fi] == "S":
            return visited[fj][fi] - 1
        
        # 네방향 탐색
        dj = [-1, 0, 1, 0]
        di = [0, 1, 0, -1]

        for k in range(4):
            nj = j + dj[k]
            ni = i + di[k]

            # 숲을 벗어나지 않고
            if 0 <= nj < R and 0 <= ni < C:
                # 미방문 + 현 위치가 고슴도치 + 다음 위치가 빈칸 or 비버의 굴인 경우
                # 걸린시간 + 1
                # 해당 위치를 고슴도치가 지나갔다고 표시
                # Q에 위치를 추가
                if not visited[nj][ni] and forest[j][i] == "S" and (forest[nj][ni] == "." or forest[nj][ni] == "D"):
                    visited[nj][ni] = visited[j][i] + 1
                    forest[nj][ni] = "S"
                    q.append((nj, ni))
                
                # 현 위치가 물이 차있는 지역 + 다음 위치가 빈칸 or 고슴도치의 위치인 경우
                # 물이 찬다
                # Q에 위치를 추가
                elif forest[j][i] == "*" and (forest[nj][ni] == "." or forest[nj][ni] == "S"):
                    forest[nj][ni] = "*"
                    q.append((nj, ni))

    # 굴에 방문하지 못 한 경우, KAKTUS 문구를 return
    return "KAKTUS"


R, C = map(int, input().split()) # 세로 R, 가로 C
forest = [list(input()) for _ in range(R)] # 티떱숩
visited = [[0] * C for _ in range(R)] # 숲 방문체크
q = deque() # 고슴도치의 위치, 물이 차있는 지역의 위치를 담을 Q


# 고슴도치의 위치를 정의, Q에 추가
# 비버의 굴 위치를 정의
for j in range(R):
    for i in range(C):
        if forest[j][i] == "S":
            sj, si = j, i
            q.append((j, i))
        elif forest[j][i] == "D":
            fj, fi = j, i

# 물이 차있는 지역의 위치를 Q에 추가
for j in range(R):
    for i in range(C):
        if forest[j][i] == "*":
            q.append((j, i))

# 고슴도치의 위치에서 시작
print(escape_forest(sj, si))
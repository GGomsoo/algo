# 불
# 골드 IV
# . 빈 공간 / # 벽 / @ 상근이의 시작 위치 / * 불

from collections import deque

def escape_fire(j, i):
    visited[j][i] = 1

    while q:
        j, i = q.popleft()

        if building[j][i] == "@" and ((j == H-1 or j == 0) or (i == W-1 or i == 0)): # 상근이가 무사히 빌딩의 끝부분에 도착했다면
            return visited[j][i] # 걸린 시간 return
        
        # 네방향 탐색
        dj = [-1, 0, 1, 0]
        di = [0, 1, 0, -1]

        for k in range(4):
            nj = j + dj[k]
            ni = i + di[k]

            # 빌딩 범위 내 있으면서
            if 0 <= nj < H and 0 <= ni < W:
                # 난 상근이고, 해당 지점 방문 안했고, 그 공간이 건물 내 빈공간이라면
                if building[j][i] == "@" and not visited[nj][ni] and building[nj][ni] == ".":
                    # 발자국 남긴다
                    building[nj][ni] = "@"
                    # 걸린시간 + 1
                    visited[nj][ni] = visited[j][i] + 1
                    q.append((nj, ni))
                
                # 난 불이고, 해당 지점이 빈 칸 or 상근이가 있던 위치라면
                elif building[j][i] == "*" and (building[nj][ni] == "." or building[nj][ni] == "@"):
                    # 불 번진다
                    building[nj][ni] = "*"
                    q.append((nj, ni))
    
    # 탈출 못하면 아래 문구 출력
    return "IMPOSSIBLE"
                

T = int(input())
for _ in range(T):
    W, H = map(int, input().split()) # 너비, 높이
    building = [list(input()) for _ in range(H)] # 빌딩에 대한 정보
    visited = [[0] * W for _ in range(H)] # 방문체크
    q = deque() # 상근이의 위치, 불의 위치를 넣을 Q

    for j in range(H):
        for i in range(W):
            if building[j][i] == "@": # 상근이의 위치
                sj, si = j, i
                q.append((j, i))
                break # 상근이는 빌딩에 한 명 뿐이다
    
    for j in range(H):
        for i in range(W):
            if building[j][i] == "*":
                q.append((j, i))
    
    print(escape_fire(sj, si))
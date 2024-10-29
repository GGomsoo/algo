# 상범 빌딩
# 골드 V
# 벽 # / 길 . / 시작 S / 출구 E

from collections import deque

def sangbum_building(l, r, c):
    visited[l][r][c] = 1
    q = deque([(l, r, c)])

    while q:
        l, r, c = q.popleft()

        if building[l][r][c] == "E":
            return print(f"Escaped in {visited[l][r][c] - 1} minute(s).")
        
        dl = [-1, 1, 0, 0, 0, 0]
        dr = [0, 0, -1, 0, 1, 0]
        dc = [0, 0, 0, 1, 0, -1]

        for k in range(6):
            nl = l + dl[k]
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C:
                if not visited[nl][nr][nc] and building[nl][nr][nc] != "#":
                    visited[nl][nr][nc] = visited[l][r][c] + 1
                    q.append((nl, nr, nc))
    
    return print("Trapped!")


while True:
    L, R, C = map(int, input().split())

    if (L, R, C) == (0, 0, 0):
        break

    building = []
    for _ in range(L):
        floor = [list(map(str, input().strip())) for _ in range(R)]
        building.append(floor)
        blank = input()
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]

    for l in range(L):
        for r in range(R):
            for c in range(C):
                if building[l][r][c] == "S":
                    sangbum_building(l, r, c)
    
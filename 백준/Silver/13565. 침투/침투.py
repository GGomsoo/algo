# 침투
# 실버 II
# 격자의 위쪽 = 바깥쪽 / 아래쪽 = 안쪽

from collections import deque

def percolate(j, i):
    global ans
    visited[j][i] = 1
    q = deque([(j, i)])

    while q:
        j, i = q.popleft()

        if j == M-1:
            ans = "YES"
            break

        dj = [-1, 0, 1, 0]
        di = [0, 1, 0, -1]

        for k in range(4):
            nj = j + dj[k]
            ni = i + di[k]

            if 0 <= nj < M and 0 <= ni < N:
                if not visited[nj][ni] and grid[nj][ni] == 0:
                    visited[nj][ni] = 1
                    q.append((nj, ni))

M, N = map(int, input().split()) # 세로 M, 가로 N
grid = [list(map(int, input())) for _ in range(M)] # 격자 구현
visited = [[0] * N for _ in range(M)] # 방문체크 배열
ans = "NO" # 기본값 NO

# 격자의 위쪽에서 흰색(0)인 경우에만 시작
for i in range(N):
    if grid[0][i] == 0:
        percolate(0, i)

print(ans)
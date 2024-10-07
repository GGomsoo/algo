# 점프왕 쩰리
# 실버 IV

from collections import deque

def jumpking(j, i):
    visited[j][i] = 1
    q = deque([(j, i)])

    while q:
        j, i = q.popleft()

        if (j, i) == (N-1, N-1):
            return "HaruHaru"
        
        dj = [1, 0]
        di = [0, 1]

        for k in range(2):
            nj = j + dj[k] * jelly[j][i]
            ni = i + di[k] * jelly[j][i]

            if 0 <= nj < N and 0 <= ni < N:
                if not visited[nj][ni]:
                    visited[nj][ni] = 1
                    q.append((nj, ni))
    
    return "Hing"

N = int(input())
jelly = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

print(jumpking(0, 0))
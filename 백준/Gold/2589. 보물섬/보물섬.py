# 보물섬
# 골드 V
from collections import deque

def solution(y, x):
    visited = [[0] * M for _ in range(N)]
    visited[y][x] = 1
    q = deque([(y, x)])

    while q:
        y, x = q.popleft()
        
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx] and maps[ny][nx] == "L":
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))
    
    return visited[y][x] - 1

N, M = map(int, input().split())
maps = [list(input()) for _ in range(N)]

shortest_time = 0

for j in range(N):
    for i in range(M):
        if maps[j][i] == "L":
            shortest_time = max(shortest_time, solution(j, i))

print(shortest_time)
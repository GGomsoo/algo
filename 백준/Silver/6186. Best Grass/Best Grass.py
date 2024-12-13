# Best Grass
# 실버 V

from collections import deque

def find_grass(i, j):
    visited[i][j] = 1
    q = deque()
    q.append((i, j))

    while q:
        i, j = q.popleft()

        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < R and 0 <= nj < C:
                if not visited[ni][nj] and farm[ni][nj] == "#":
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))

R, C = map(int, input().split())
farm = [list(map(str, input())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
result = 0

for i in range(R):
    for j in range(C):
        if not visited[i][j] and farm[i][j] == "#":
            find_grass(i, j)
            result += 1

print(result)
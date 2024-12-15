# 양 한마리... 양 두마리...
# 실버 II

from collections import deque

def count_sheep(i, j):
    visited[i][j] = 1
    farm[i][j] = '.'
    q = deque([(i, j)])

    while q:
        i, j = q.popleft()

        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < H and 0 <= nj < W:
                if not visited[ni][nj] and farm[ni][nj] == '#':
                    visited[ni][nj] = visited[i][j] + 1
                    farm[ni][nj] = '.'
                    q.append((ni, nj))

T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    farm = [list(input()) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]

    result = 0
    for i in range(H):
        for j in range(W):
            if farm[i][j] == '#':
                count_sheep(i, j)
                result += 1

    print(result)
    
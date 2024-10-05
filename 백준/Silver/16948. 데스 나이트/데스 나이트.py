# 데스 나이트
# 실버 I

from collections import deque

def bfs(c, r):
    visited[c][r] = 1
    q = deque([(c, r)])

    while q:
        c, r = q.popleft()

        if (c, r) == (c2, r2):
            return visited[c][r] - 1
        
        # 문제에 제시된 순서대로 해야한다.
        dc = [-1, 1, -2, 2, -1, 1]
        dr = [-2, -2, 0, 0, 2, 2]

        for k in range(6):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nc < N and 0 <= nr < N:
                if not visited[nc][nr]:
                    visited[nc][nr] = visited[c][r] + 1
                    q.append((nc, nr))
    
    return -1

N = int(input()) # 체스판의 크기 N
r1, c1, r2, c2 = map(int, input().split())

visited = [[0] * N for _ in range(N)]

print(bfs(c1, r1))
# 불!
# 골드 III
# # 벽 / . 공간 / J 지훈이 초기위치 / F 불 난 공간
from collections import deque

def escape_fire(j, i):
    visited[j][i] = 1

    while q:
        j, i = q.popleft()

        if maze[j][i] == "J" and ((j == 0 or j == R-1) or (i == 0 or i == C-1)):
            return print(visited[j][i])
        
        dj = [-1, 0, 1, 0]
        di = [0, 1, 0, -1]

        for k in range(4):
            nj = j + dj[k]
            ni = i + di[k]

            if 0 <= nj < R and 0 <= ni < C:
                if maze[j][i] == "J" and not visited[nj][ni] and maze[nj][ni] == ".":
                    maze[nj][ni] = "J"
                    visited[nj][ni] = visited[j][i] + 1
                    q.append((nj, ni))
                
                elif maze[j][i] == "F" and (maze[nj][ni] == "J" or maze[nj][ni] == "."):
                    maze[nj][ni] = "F"
                    q.append((nj, ni))
    
    return print("IMPOSSIBLE")



R, C = map(int, input().split())
maze = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
q = deque()

for j in range(R):
    for i in range(C):
        if maze[j][i] == "J":
            sj, si = j, i
            q.append((j, i))

for j in range(R):
    for i in range(C):
        if maze[j][i] == "F":
            q.append((j, i))

escape_fire(sj, si)
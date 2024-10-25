from collections import deque

M, N = map(int, input().split()) # 상자의 가로M, 세로N

tmt = [list(map(int, input().split())) for _ in range(N)]
q = deque([])
time = 0

for j in range(N):
    for i in range(M):
        if tmt[j][i] == 1:
            q.append((j, i))

def solution():
    while q:
        j, i = q.popleft()

        dj = [-1, 0, 1, 0]
        di = [0, 1, 0, -1]

        for k in range(4):
            nj = j + dj[k]
            ni = i + di[k]

            if 0 <= nj < N and 0 <= ni < M:
                if tmt[nj][ni] == 0:
                    tmt[nj][ni] = tmt[j][i] + 1
                    q.append((nj, ni))

solution()

for mato in tmt:
    if 0 in mato:
        print(-1)
        exit(0) # 코드 완전 탈출
    time = max(time, *mato)
print(time - 1)
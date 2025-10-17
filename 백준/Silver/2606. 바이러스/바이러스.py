N = int(input()) # 컴퓨터의 수
M = int(input()) # 연결된 컴퓨터 쌍의 수

def solution(v):
    global ans
    visited[v] = 1
    ans += 1

    for w in range(1, N+1):
        if not visited[w] and linked[v][w]:
            solution(w)


linked = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
ans = 0

for _ in range(M):
    s, e = map(int, input().split())
    linked[s][e] = linked[e][s] = 1

solution(1)
print(ans - 1)
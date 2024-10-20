# 폴짝폴짝
# 실버 II

from collections import deque

def poljjak(v):
    visited[v] = 1
    q = deque([v])

    while q:
        v = q.popleft()

        if v == B-1:
            return visited[v] - 1
        
        # A < B
        for w in range(v, N, bridge[v]):
            if not visited[w]:
                visited[w] = visited[v] + 1
                q.append(w)

        # A > B
        for x in range(v, -1, -bridge[v]):
            if not visited[x]:
                visited[x] = visited[v] + 1
                q.append(x)
    
    return -1

N = int(input())
bridge = list(map(int, input().split()))
A, B = map(int, input().split())

visited = [0] * N

print(poljjak(A-1))
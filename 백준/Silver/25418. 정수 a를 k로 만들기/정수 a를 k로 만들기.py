# 정수 a를 k로 만들기
# 실버 III

from collections import deque

def make_k(v):
    visited[v] = 1
    q = deque([v])

    while q:
        v = q.popleft()
        if v == K:
            return visited[v] - 1
        
        for w in (v+1, v*2):
            if not visited[w] and w <= K:
                visited[w] = visited[v] + 1
                q.append(w)

A, K = map(int, input().split())
visited = [0] * (K*2+1)
print(make_k(A))
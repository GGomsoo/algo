# 요세푸스 문제
# 실버 IV
# N명의 사람 중 K번째 사람을 제거
# N명의 사람이 모두 제거될 때 까지 진행

from collections import deque

N, K = map(int, input().split())

Q = deque(list(range(1, N+1))) # N명의 사람들
ans = deque() # 제거된 순서

while Q:
    for _ in range(K-1): # 제거대상 이전까지 사람들을 Q위 뒤로 보낸다
        Q.append(Q.popleft())
    ans.append(Q.popleft()) # K번째 순서인 사람을 제거

print("<", end="")
print(*ans, sep=", ", end="")
print(">")
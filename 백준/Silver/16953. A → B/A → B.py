# A -> B
# 실버 II
# A를 B로 바꾸는데 필요한 연산의 최솟값
from collections import deque

def bfs(v, cnt):
    q = deque([(v, cnt)])

    while q:
        v, cnt = q.popleft()

        if v > B: # 연산값이 목표값인 B보다 커진 경우 넘긴다
            continue

        if v == B:
            return cnt
        
        v2 = v * 2 # 2를 곱한다
        v1 = int(str(v) + "1") # 1을 수의 가장 오른쪽에 추가한다

        # 해당 숫자들을 q에 넣는다
        q.append((v2, cnt + 1))
        q.append((v1, cnt + 1))
    
    return -1

A, B = map(int, input().split())

print(bfs(A, 1))
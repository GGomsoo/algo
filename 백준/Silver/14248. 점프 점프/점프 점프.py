# 점프 점프
# 실버 II

from collections import deque

def jump_jump(v):
    global cnt
    visited[v] = 1 # 방문처리
    q = deque([v]) # Q에 추가

    while q:
        v = q.popleft()

        for w in (v-stone_bridge[v], v+stone_bridge[v]): # 현재 위치 - 현재 위치의 돌 값, 현재 위치 + 현재 위치의 돌 값
            if 0 <= w < N and not visited[w]: # 점프하는 위치가 범위 내에 있으면서, 방문 안 한 돌이라면
                visited[w] = 1 # 방문 처리
                cnt += 1 # 방문한 돌 갯수 추가
                q.append(w) # q에 추가

N = int(input()) # 돌 갯수
stone_bridge = list(map(int, input().split())) # 돌
S = int(input()) # 시작점

visited = [0] * N # 방문체크
cnt = 1 # 방문한 돌 갯수

jump_jump(S-1) # S는 index로 활용하기 때문에 -1을 해준다
print(cnt)
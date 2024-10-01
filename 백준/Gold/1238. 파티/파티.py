# 파티
# 골드 III
# 다익스트라

import heapq

def party(v):
    distance = [float("INF")] * (N+1) # 함수 내에서 거리 배열을 관리
    heap = []
    heapq.heappush(heap, (0, v)) # 걸리는 시간, 위치를 힙에 추가
    distance[v] = 0 # 시작 지점 초기화

    while heap:
        time, position = heapq.heappop(heap)

        if distance[position] < time:
            continue

        for w in adj[position]:
            next_ = w[0]
            time_ = w[1]

            use_time = time + time_
            if distance[next_] <= use_time:
                continue

            distance[next_] = use_time
            heapq.heappush(heap, (use_time, next_))
    
    return distance


N, M, X = map(int, input().split()) # N명의 학생, M개의 단방향 도로, X번 마을
adj = [[] for _ in range(N+1)] # 인접 리스트

for _ in range(M):
    start, end, time = map(int, input().split()) # 출발, 도착, 걸리는 시간
    adj[start].append((end, time))

ans = 0
for i in range(1, N+1): # 1번부터 N번까지의 학생들을 조사
    go_party = party(i) # i번 학생이 파티로 출발
    go_home = party(X) # X 위치에서 집으로 출발
    ans = max(ans, go_party[X] + go_home[i]) # 기존 ans값, X번 마을까지 가는 시간 + i번 마을로 돌아오는 시간 중 최대값 비교

print(ans)
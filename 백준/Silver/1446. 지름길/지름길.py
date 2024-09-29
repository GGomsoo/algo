# 지름길
# 실버 I

import heapq

def solution(v):
    heap = [] # 힙 배열 생성
    heapq.heappush(heap, (0, v)) # 다음 도로까지의 거리, 현재지점을 힙에 넣는다
    distance[v] = 0 # 시작지점 0으로 초기화

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist: # 현재 위치까지 더 짧게 온 적이 있다면 넘어간다
            continue

        for w in adj[now]: # 인접 리스트 활용
            next_location = w[0] # 다음 위치
            cost = w[1] # 그 위치까지 가는데의 거리

            next_cost = dist + cost # 지금까지 온 거리 + 다음위치까지 가는 거리
            if distance[next_location] <= next_cost: # 위 길이보다 더 짧게 온 적이 있다면 넘어간다
                continue

            distance[next_location] = next_cost
            heapq.heappush(heap, (next_cost, next_location))



N, D = map(int, input().split()) # 지름길의 갯수 N, 고속도로의 길이 D
distance = [float("INF")] * (D+1) # 고속도로의 길이만큼 배열을 생성, 무한대의 값으로 채워넣는다
adj = [[] for _ in range(D+1)] # 고속도로의 길이만큼 인접 리스트 생성

for i in range(D): # 지름길이 아닌 일반도로에 대한 정보를 채워넣는다
    adj[i].append([i+1, 1])

for _ in range(N): # 지름길에 대한 정보
    start, end, long = map(int, input().split())

    # 지름길 종료지점이 고속도로 전체 길이보다 작거나 같고
    # 지름길 시작이 끝보다 작고
    # 지름길의 길이가 지름길의 끝과 시작의 차이보다 작은 경우만 인접 리스트에 채워넣는다
    if end <= D and start < end and long < end - start: 
        adj[start].append([end, long])

solution(0)
print(distance[D])
# 최소비용 구하기
# 골드 V

import heapq

def bus_cost(v):
    heap = [] # 힙 배열 생성
    heapq.heappush(heap, (0, v)) # 초기 비용, 초기 출발지점을 힙에 추가
    distance[v] = 0 # 초기 위치 초기화

    while heap:
        c, now = heapq.heappop(heap) # 비용, 현재지점을 힙에서 추출

        if distance[now] < c: # 힙에서 추출한 비용보다 더 저렴하게 오는 방법이 있었다면
            continue

        for w in adj[now]: # 인접 리스트에서 다음 도착지, 비용 정보를 얻는다
            next = w[0]
            pay = w[1]

            next_pay = c + pay # 다음 위치까지 가는 비용 = 현재까지 오는 비용 + 현재->다음 가는 비용

            if distance[next] <= next_pay: # 해당 비용보다 저렴하게 오는 방법이 있었다면 계속 진행한다
                continue

            distance[next] = next_pay # 없었다면 해당 위치까지 오는데 있어서, 이 방법이 제일 저렴하다
            heapq.heappush(heap, (next_pay, next)) # 비용과 도시정보를 힙에 추가

N = int(input()) # 도시의 갯수 N
M = int(input()) # 버스의 갯수 M

distance = [float("INF")] * (N+1)
adj = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split()) # 출발 도시, 도착 도시, 비용
    adj[start].append((end, cost)) # 인접 리스트에 추가

S, E = map(int, input().split()) # 구하고자 하는 출발점, 도착점의 도시 번호
bus_cost(S) # 구하려는 시작지점을 함수에 넣는다
print(distance[E]) # 구하려는 도착지점을 출력한다 
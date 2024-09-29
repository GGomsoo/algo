# 최단경로
# 골드 IV
import heapq
import sys; input = sys.stdin.readline

def shortest(v):
    heap = []
    heapq.heappush(heap, (0 ,v))
    distance[v] = 0

    while heap:
        weight, now = heapq.heappop(heap)

        if distance[now] < weight:
            continue

        for w in adj[now]:
            next = w[0]
            cost = w[1]

            next_weight = weight + cost
            if distance[next] <= next_weight:
                continue

            distance[next] = next_weight
            heapq.heappush(heap, (next_weight, next))

V, E = map(int, input().split())
K = int(input())

distance = [float("INF")] * (V+1)
adj = [[] for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    adj[s].append((e, w))

shortest(K)

for i in range(1, V+1):
    print(str(distance[i]).upper())
# 치킨 배달
# 골드 V
## 0 빈칸 / 1 집 / 2 치킨집
## 다시 풀어보자
from collections import deque

def chicken_delivery(idx, cnt):
    global min_chicken_dist

    if cnt == M:
        result = 0
        for h in house:
            temp_dist = float("INF")
            for c in range(len(chicken)):
                if visited[c]:
                    chicken_dist = abs(h[1] - chicken[c][1]) + abs(h[0] - chicken[c][0])
                    temp_dist = min(chicken_dist, temp_dist)
            result += temp_dist
        min_chicken_dist = min(result, min_chicken_dist)
        return

    for i in range(idx, len(chicken)):
        if not visited[i]:
            visited[i] = 1
            chicken_delivery(i+1, cnt+1)
            visited[i] = 0

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

house = deque()
chicken = deque()
min_chicken_dist = float("INF")

for j in range(N):
    for i in range(N):
        if city[j][i] == 1:
            house.append((j, i))
        elif city[j][i] == 2:
            chicken.append((j, i))

visited = [0] * len(chicken)

chicken_delivery(0, 0)
print(min_chicken_dist)
# 뱀과 사다리 게임
# 골드 V

from collections import deque
# import sys; input = sys.stdin.readline

def game(v):
    used[v] = 1
    q = deque([v])

    while q:
        now = q.popleft()

        if now == 100:
            return used[now] - 1
        
        for dice in range(1, 7):
            new_location = now + dice

            if new_location <= 100 and not used[new_location]:
                if new_location in ladders:
                    new_location = ladders[new_location]
                
                if new_location in snakes:
                    new_location = snakes[new_location]
                
                if not used[new_location]:
                    used[new_location] = used[now] + 1
                    q.append(new_location)

N, M = map(int, input().split())
used = [0] * 101

ladders = {}
for _ in range(N):
    x, y = map(int, input().split())
    ladders[x] = y

snakes = {}
for _ in range(M):
    u, v = map(int, input().split())
    snakes[u] = v

print(game(1))
from collections import deque
import sys; input = sys.stdin.readline

N, W, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))
bridge = deque([0] * W)
sec = 0

while bridge:
    sec += 1
    first = bridge.popleft()

    if trucks:
        if sum(bridge) + trucks[0] <= L:
            truck = trucks.popleft()
            bridge.append(truck)
        else:
            bridge.append(0)

print(sec)
# 절댓값 힙
# 실버 I
# 배열에 정수 x (x != 0 ) 를 넣는다.
# 배열에서 절댓값이 가장 작은 값을 출력, 그 값을 배열에서 제거
## 절댓값이 가장 작은 값이 여러개일땐, 가장 작은 수를 출력. 값을 배열에서 제거

import sys; input = sys.stdin.readline
import heapq

N = int(input())
hq = []

for _ in range(N):
    num = int(input())

    if num != 0:
        heapq.heappush(hq, (abs(num), num))
    else:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
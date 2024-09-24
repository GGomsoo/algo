# 최소 힙
# 실버 II
import heapq
import sys; input = sys.stdin.readline

N = int(input()) # 연산의 갯수
hq = [] # 힙큐

for _ in range(N):
    num = int(input()) # 자연수 입력받고

    if num == 0: # 숫자가 0 인데
        if len(hq) == 0: # 배열이 비어있다면
            print(0) # 0을 출력
        else: # 비어있지 않다면
            print(heapq.heappop(hq)) # 최솟값을 출력
    
    elif num > 0: # 0보다 크다면
        heapq.heappush(hq, num) # 해당 값을 배열에 삽입
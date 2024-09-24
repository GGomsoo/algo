# 최대 힙
# 실버 II
# 최댓값을 출력하는 문제

import heapq
import sys; input = sys.stdin.readline

N = int(input()) # 연산의 갯수
hq = [] # heapq

for _ in range(N):
    num = int(input()) # 자연수 입력받음

    if num != 0:
        heapq.heappush(hq, -num) # 입력받은 자연수의 부호를 바꾸어 배열에 삽입
    
    else:
        if hq: # 배열에 숫자가 있다면
            print(-heapq.heappop(hq)) # 최솟값의 부호를 다시 바꾼 후 출력 ( = 최댓값 출력 )
            # 자연수는 0보다 크고 2**31보다는 작다.
        else:
            print(0)
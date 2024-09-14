# DSLR
# 골드 IV
from collections import deque
import sys; input = sys.stdin.readline

def DSLR(num, order):
    visited = [0] * 10000
    visited[num] = 1
    q = deque([(num, order)])

    while q:
        num, order = q.popleft()

        if num == B:
            return order
        
        # D 연산
        D = (num * 2) % 10000
        if not visited[D]:
            visited[D] = 1
            q.append((D, order + "D"))

        # S 연산
        S = 9999 if num == 0 else num - 1
        if not visited[S]:
            visited[S] = 1
            q.append((S, order + "S"))

        # L 연산
        # temp_L = str(num)
        # L_lst = []
        # for i in range(len(temp_L)):
        #     L_lst += temp_L[i]
        
        # L_lst.append(L_lst.pop(0))
        # L = int("".join(L_lst))
        L = (num % 1000) * 10 + (num // 1000)
        if not visited[L]:
            visited[L] = 1
            q.append((L, order + "L"))

        # R 연산
        # temp_R = str(num)
        # R_lst = deque([])
        # for x in range(len(temp_R)):
        #     R_lst += temp_R[x]
        
        # R_lst.appendleft(R_lst.pop())
        # R = int("".join(R_lst))
        R = ((((num % 1000) % 100) % 10) * 1000) + (num // 10)
        if not visited[R]:
            visited[R] = 1
            q.append((R, order + "R"))

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(DSLR(A, ""))